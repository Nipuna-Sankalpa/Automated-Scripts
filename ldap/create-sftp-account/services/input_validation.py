import re
import socket

from validate_email import validate_email


def input_validation(input_key, input_value):
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if input_key == "clientType":
        if input_value == "onsite" or input_value == "cloud":
            return True
        return False
    elif input_key == "accountType":
        if input_value == "temporary" or input_value == "permenant":
            return True
        return False
    elif input_key == "requesterEmailAddress":
        if re.search(email_regex, input_value) and validate_email(input_value, check_mx=True, verify=True):
            return True
        return False


def resolve_domain_name(domain_name):
    ip_address = socket.gethostbyname(domain_name)
    return ip_address
