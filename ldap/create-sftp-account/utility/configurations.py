import os

import yaml


def get_remote_user():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'), yaml.SafeLoader)
    configuration_values = configuration_object['remote_server_login_details']
    return {'user_name': configuration_values[0]['remote_user'], 'password': configuration_values[0]['remote_password']}


def get_predefined_input_parameters():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'), yaml.SafeLoader)
    configuration_values = configuration_object['input_parameters']
    return configuration_values


def get_email_settings():
    yaml_input = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'), yaml.SafeLoader)
    return yaml_input['email_configurations']


def get_only_predefined_input_parameters():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'), yaml.SafeLoader)
    configuration_values = configuration_object['input_parameters']
    parameter_list = []
    for configuration_value in configuration_values:
        parameter_list.append(configuration_value['key'])
    return parameter_list


def get_ldap_configuration_details():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'), yaml.SafeLoader)
    configuration_values = configuration_object['ldap_directory_details']
    return configuration_values
