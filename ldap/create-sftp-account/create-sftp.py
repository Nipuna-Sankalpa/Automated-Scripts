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
    input_key_list = get_input_parameters()
    yaml_input = yaml.load(open("input.yml"))

    if yaml_input == None:
        separator()
        print("Input Parameter File is empty/not available. Please continue with the runtime inputs")
        separator()
        print("SFTP Account Details :")
        for i in range(len(input_key_list)):
            print("Tips : " + input_key_list[i]['help_text'])
            tmp = input(input_key_list[i]['display_name'] + " : ")
            input_object[input_key_list[i]['key']] = tmp



def main():
    print()
    # get input
    # validate input
    # create ldap account
    # create home directory
    # send email


get_input()
