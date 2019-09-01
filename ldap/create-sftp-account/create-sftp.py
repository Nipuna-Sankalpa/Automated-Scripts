import yaml

# ldap credentials
ldap_host = ""
ldap_port = ""
ldap_bind_user_name = ""
ldap_bind_user_password = ""
input_file_name = ""


def get_input():
    yaml_input = yaml.load(open("input.yml"))
    print(yaml_input)


def main():
    print()
    # get input
    # validate input
    # create ldap account
    # create home directory
    # send email
