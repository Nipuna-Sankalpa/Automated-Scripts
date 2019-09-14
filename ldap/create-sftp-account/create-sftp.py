from datetime import datetime

from services.directory_operations import *
from services.input_validation import *
from services.ldap_operations import *
from utility.SFTP_creation_mail import *
from utility.configurations import *


def separator():
    print("=======================================================================")


def get_input():
    input_object = {}
    input_object_list = []
    input_key_list = get_predefined_input_parameters()

    yaml_input = yaml.load(open("input.yml"), yaml.SafeLoader)

    # if inout file totally invalid
    if yaml_input == None:
        separator()
        print("Input Parameter File is empty/not available. Please continue with the runtime inputs")
        separator()
        print("SFTP Account Details :")
        separator()
        for i in range(len(input_key_list)):
            if input_key_list[i]['key'] == 'validityPeriod' and input_object['accountType'] == 'permenant':
                print("Validity period is not required since account type is permanent")
            else:
                print("Tips : " + input_key_list[i]['help_text'])
                tmp = input(input_key_list[i]['display_name'] + " : ")
                while True:
                    if input_validation(input_key_list[i]['key'], tmp):
                        input_object[input_key_list[i]['key']] = tmp
                        break
                    else:
                        print("Incorrect input. please re-enter")
                        tmp = input(input_key_list[i]['display_name'] + " : ")
        input_object_list.append(input_object)
    else:
        # if input file contains partial values
        input_object_list = yaml_input['sftpAccounts']
        input_key_list = get_only_predefined_input_parameters()

        for input_object in input_object_list:
            object_key_list = list(input_object.keys())
            for key in input_key_list:
                if key in object_key_list:
                    if not input_validation(key, input_object[key]):
                        print(input_object)
                        while True:
                            print(key + " is incorrect in the above object. Please add correct value")
                            tem_input_val = input(key + ' : ')
                            if input_validation(key, tem_input_val):
                                break
                        input_object[key] = tem_input_val
                else:
                    print(key + " is not available in the input file. Please enter value below")
                    tem_input_val = input(key + ' : ')
                    if not input_validation(key, tem_input_val):
                        while True:
                            print(key + " is incorrect. Please add correct value")
                            tem_input_val = input(key + ' : ')
                            if input_validation(key, tem_input_val):
                                break
                        input_object[key] = tem_input_val

    return input_object_list


def main():
    ldap_configurations_details = get_ldap_configuration_details()
    ldap_host = ldap_configurations_details['ldap_host']
    ldap_port = ldap_configurations_details['ldap_port']
    ldap_bind_user_name = ldap_configurations_details['ldap_bind_user_name']
    ldap_bind_user_password = ldap_configurations_details['ldap_bind_user_password']

    separator()
    print("Collecting Inputs ...")
    input_object_list = get_input()
    print("Connecting to LDAP ...")
    ldap_connection = ldap_connect(ldap_host, ldap_port, 'ldaps')
    connection_status = ldap_connection.simple_bind_s(ldap_bind_user_name, ldap_bind_user_password)
    if connection_status:
        print("Connected to " + ldap_host)
    else:
        print("LDAP Connection fail. Please re-check the availability of the LDAP server")
        return False

    print("Creating SFTP Account(s) ...")
    for input_object in input_object_list:
        user_password = generate_password()
        uid_number = get_new_uid_number(ldap_connection)
        server_ip = resolve_domain_name(input_object['serverIP'])
        server_name = get_server_name(server_ip)
        client_display_name = input_object['username'].capitalize()

        user_status = ldap_add_user(ldap_connection, input_object['username'], client_display_name,
                                    uid_number, server_name,
                                    input_object['accountType'], user_password['ldap_password'])

        if user_status == "duplications":
            print("*** " + client_display_name + " user account already exist")
            return False
        elif user_status:
            print("*** " + client_display_name + " added to LDAP directory")
        else:
            print(client_display_name + " failed to add LDAP directory")
            return False

        groups_status = authorize_sftp_account(input_object['username'], server_ip, ldap_connection)

        if groups_status:
            print("*** " + client_display_name + " was authorized to " + server_name + " server")
        else:
            print(client_display_name + " was failed to authorize into " + server_name + " server")
            return False

        if server_name == 'Artemis':
            result = create_sftp_home_directory(input_object['username'])
        else:
            result = create_remote_sftp_home_directory(input_object['username'], server_ip)

        if user_status and groups_status:
            print("*** " + "Sending success notification along with the account details")
            send_email(input_object['requesterEmailAddress'], input_object['username'], user_password['raw_password'],
                       input_object['serverIP'], '2112')
            input_object['addedDate'] = datetime.today().strftime('%Y-%m-%d')
            update_expire_dates_file(input_object)
        else:
            print("LDAP Account Creation FAIL")

    ldap_connection.unbind_s()
    # clean input file
    input_cleanup_file_path = os.path.dirname(__file__) + '/auto-generated-files/temporary_input_file.yml'
    input_file_path = os.path.dirname(__file__) + '/input.yml'
    os.system('cat ' + input_cleanup_file_path + ' > ' + input_file_path)

    # update log file
    timestamp = str(datetime.now())
    created_by = str(os.getlogin())
    log_record = timestamp + ' ' + input_object['username'] + ' ' + input_object['serverIP'] + ' ' + created_by + ' ' + \
                 input_object['requesterEmailAddress']
    log_file_name = os.path.dirname(__file__) + '/logs/create-sftp.log'
    os.system('echo "' + log_record + '" >> ' + log_file_name)
    return True


main()
