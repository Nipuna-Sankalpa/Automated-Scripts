from services.directory_operations import *
from services.input_validation import *
from services.ldap_operations import *
from utility.configurations import *

# ldap credentials
ldap_host = ""
ldap_port = ""
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
    input_object_list = get_input()
    ldap_connection = ldap_connect(ldap_host, ldap_port)
    ldap_connection.simple_bind_s(ldap_bind_user_name, ldap_bind_user_password)
    for input_object in input_object_list:
        user_password = generate_password()
        uid_number = get_new_uid_number(ldap_connection)
        server_ip = resolve_domain_name(input_object['serverIP'])
        server_name = get_server_name(server_ip)

        output = ldap_add_user(ldap_connection, input_object['username'], "client_name", uid_number, server_name,
                               input_object['accountType'], user_password['ldap_password'])
        authorize_sftp_account(input_object['username'], server_ip, ldap_connection)
        if server_name == 'Artemis':
            result = create_sftp_home_directory(input_object['username'])
        else:
            result = create_remote_sftp_home_directory(input_object['username'], server_ip)

    ldap_connection.unbind_s()


print(get_input())
