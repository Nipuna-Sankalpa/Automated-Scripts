from services.input_validation import *
from services.ldap_operations import *
from utility.configurations import *

# ldap credentials
ldap_host = ""
ldap_port = ""
ldap_bind_user_name = ""
ldap_bind_user_password = ""
input_file_name = ""


def separator():
    print("=======================================================================")


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

    for input_object in input_object_list:
        ldap_add_user()
        input_object


print(get_input())
