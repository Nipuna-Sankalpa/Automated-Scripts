import socket


def input_validation(input_key, input_value):
    print(input_key)


def resolve_domain_name(domain_name):
    ip_address = socket.gethostbyname(domain_name)
    return ip_address
