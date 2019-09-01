import base64
import binascii
import hashlib
import random
import string

import ldap
import ldap.modlist as modlist
import yaml


def generate_password():
    raw_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    sha256_pwd = hashlib.sha256(bytes(raw_password, 'utf-8')).hexdigest()
    ldap_password = "{SHA-256}" + base64.b64encode(binascii.unhexlify(sha256_pwd)).decode('utf-8')
    return {"raw_password": raw_password, "ldap_password": ldap_password}


def ldap_connect(domain_name, port, protocol):
    connection = ldap.initialize(protocol + "://" + domain_name + ":" + port + "/")
    return connection


def get_new_uid_number(ldap_connection):
    query = "(uid=*)"
    ldap_base = "ou=clients,ou=users,dc=orangehrm,dc=com"
    uid_number_list = []
    output = ldap_connection.search_s(ldap_base, ldap.SCOPE_SUBTREE, query, ['uidNumber'])
    if not len(output) >= 0:
        return False

    for i in output:
        uid_number = output[i][1]['uidNumber'][0].decode('utf-8')
        uid_number_list.append(uid_number)

    uid_number_integer_list = list(map(int, uid_number_list))
    uid_number_integer_list.sort()
    last_available_uid_number = uid_number_integer_list.pop()
    new_uid_number = last_available_uid_number + 1

    # check for the availability of new uid number
    while True:
        ldap_base = "ou=users,dc=orangehrm,dc=com"
        query = "(uidNumber=" + new_uid_number + ")"
        output = ldap_connection.search_s(ldap_base, ldap.SCOPE_SUBTREE, query, ['uidNumber'])
        if len(output) <= 0:
            break
        new_uid_number = new_uid_number + 1
    return new_uid_number


def ldap_add_user(ldap_connection, user_name, client_name, uid_number, server_name, account_type, user_password):
    dn = "uid={{user_name}},ou={{account_type}},ou=clients,ou=users,dc=orangehrm,dc=com"
    dn = dn.replace("{{user_name}}", user_name)
    dn = dn.replace("{{account_type}}", account_type)
    home_directory = "/ftp/" + user_name

    user_name = bytes(user_name, 'utf-8')
    client_name = bytes(client_name, 'utf-8')
    uid_number = bytes(uid_number, 'utf-8')
    server_name = bytes(server_name, 'utf-8')
    home_directory = bytes(home_directory, 'utf-8')
    user_password = bytes(user_password, 'utf-8')

    mod_list = {
        "objectClass": [b"top", b"posixAccount", b"inetOrgPerson", b"organizationalPerson", b"person",
                        b"shadowAccount"],
        "uid": [user_name],
        "sn": [b"FTP"],
        "cn": [user_name],
        "description": [b"An sftp user"],
        "displayName": [client_name],
        "uidNumber": [uid_number],
        "gidNumber": [b"8600"],
        "labeledURI": [server_name],
        "loginShell": [b"/bin/bash"],
        "userPassword": [user_password],
        "homeDirectory": [home_directory]
    }

    result = ldap_connection.add_s(dn, modlist.addModlist(mod_list))
    return result


def ldap_delete_user(ldap_connection, rdn):
    result = ldap_connection.delete_s(rdn)
    return result


def search_ldap_user(ldap_connection, uid, ldap_base):
    query = "(uid=" + uid + ")"
    result = ldap_connection.search_s(ldap_base, ldap.SCOPE_BASE, query)
    return result


# add sftp user into respective authorize user group
def authorize_sftp_account(user_name, server_ip, ldap_connection):
    yaml_input = yaml.load(open("../auto-generated-files/server_name_mapping.yml"))
    server_ip_mapping = yaml_input['ohrmCloud']
    server_nick_name = ""
    for x in server_ip_mapping:
        if x['ip'] == server_ip:
            server_nick_name = x['name']

    if server_nick_name == "":
        return False

    dn = "cn=authorized,ou={{server_name}},ou=servers,ou=groups,dc=orangehrm,dc=com"
    dn = dn.replace('{{server_name}}', server_nick_name.lower())
    # memberUid
    user_name = bytes(user_name, 'utf-8')
    ldap_connection.modify_s(dn, [(0, 'memberUid', user_name)])

# l = ldap.initialize("ldaps://dev-ldap.orangehrm.com:636/")
# l.simple_bind_s("cn=admin,dc=orangehrm,dc=com", "pL32Fk7UxU2o")
# # password = generate_password()['ldap_password']
# result = get_new_uid_number(l)
# # print(result[0][1]['uidNumber'][0].decode('utf-8'))
# print(result)

# authorize_sftp_account('sankalpa', '161.47.68.144', l)
# l.unbind_s()
