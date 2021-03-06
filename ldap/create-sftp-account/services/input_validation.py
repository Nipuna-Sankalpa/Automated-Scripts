import os
import re
import socket

import yaml
from validate_email import validate_email

from utility.constants import *


def input_validation(input_key, input_value):
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if input_key == "clientType":
        if input_value == "onsite" or input_value == "cloud":
            return True
        return False
    elif input_key == "accountType":
        if input_value == account_type_temporary or input_value == account_type_permanent:
            return True
        return False
    elif input_key == "username":
        if input_key is not '' and input_key is not None:
            return True
        return False
    elif input_key == "requesterEmailAddress":
        if re.search(email_regex, input_value) and validate_email(input_value, check_mx=True, verify=True):
            return True
        return False
    elif input_key == "validityPeriod":
        try:
            int_value = int(input_value)
            if type(int_value) == int and int_value > 0:
                return True
            return False
        except:
            return False
    elif input_key == "serverIP":
        ip = resolve_domain_name(input_value)
        server_object_list = load_registered_server_list()
        for server_object in server_object_list:
            if ip and ip == server_object['ip']:
                return True
        return False
    else:
        return True


def resolve_domain_name(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
    except:
        return False
    return ip_address


def load_registered_server_list():
    yaml_input = yaml.load(open(os.path.dirname(__file__) + "/../auto-generated-files/server_name_mapping.yml"),
                           yaml.SafeLoader)
    return yaml_input['ohrmCloud']


def get_server_name(ip):
    server_list = load_registered_server_list()
    for server_object in server_list:
        if ip and ip == server_object['ip']:
            return server_object['name']
    return False


def get_input_file():
    yaml_input = yaml.load(open(os.path.dirname(__file__) + "/../input.yml"), yaml.SafeLoader)
    return yaml_input
