from services.input_validation import *
from services.ldap_operations import *
from utility.SFTP_creation_mail import *
from utility.configurations import *

# ldap credentials
ldap_host = "dev-ldap.orangehrm.com"
ldap_port = "636"
ldap_bind_user_name = "cn=admin,dc=orangehrm,dc=com"
ldap_bind_user_password = "pL32Fk7UxU2o"
input_file_name = ""


def separator():
    print("=======================================================================")


# todo - ask for a validity period only if the account type is temporary
# todo - validate input from the file

def get_input():
    input_object = {}
    input_object_list = []
    input_key_list = get_input_parameters()

    yaml_input = yaml.load(open("input.yml"))

    # if inout file totally invalid
    if yaml_input == None:
        separator()
        print("Input Parameter File is empty/not available. Please continue with the runtime inputs")
        separator()
        print("SFTP Account Details :")
        separator()
        for i in range(len(input_key_list)):
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
    return input_object_list


def main():
    print("Collect Input ...")
    input_object_list = get_input()
    print("Connecting to LDAP")
    ldap_connection = ldap_connect(ldap_host, ldap_port, 'ldaps')
    connection_status = ldap_connection.simple_bind_s(ldap_bind_user_name, ldap_bind_user_password)
    if connection_status:
        print("Connecting to LDAP")
    else:
        print("LDAP Connection fail. Please check the availability of the LDAP server")
        return False

    print("Create SFTP Accounts")
    for input_object in input_object_list:
        user_password = generate_password()
        uid_number = get_new_uid_number(ldap_connection)
        server_ip = resolve_domain_name(input_object['serverIP'])
        server_name = get_server_name(server_ip)
        client_display_name = input_object['username'].capitalize()

        user_status = ldap_add_user(ldap_connection, input_object['username'], client_display_name,
                                    uid_number, server_name,
                                    input_object['accountType'], user_password['ldap_password'])
        groups_status = authorize_sftp_account(input_object['username'], server_ip, ldap_connection)

        if user_status:
            print(client_display_name + " added to LDAP directory")
        else:
            print(client_display_name + " failed to add LDAP directory")
            return False
        if groups_status:
            print(client_display_name + " was authorized to " + server_name + " server")
        else:
            print(client_display_name + " was failed to authorize into " + server_name + " server")
            return False

        # if server_name == 'Artemis':
        #     result = create_sftp_home_directory(input_object['username'])
        # else:
        #     result = create_remote_sftp_home_directory(input_object['username'], server_ip)

        if user_status and groups_status:
            send_email(input_object['requesterEmailAddress'], input_object['username'], user_password['raw_password'],
                       input_object['serverIP'], '2112')
        else:
            send_email("nipuna@orangehrmlive.com", input_object['username'], user_password['raw_password'],
                       input_object['serverIP'], '2112')
    ldap_connection.unbind_s()


print(main())
