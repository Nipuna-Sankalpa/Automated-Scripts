import os

import yaml


def get_configuration_file():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'), yaml.SafeLoader)
    return configuration_object


def get_remote_user():
    configuration_object = get_configuration_file()
    configuration_values = configuration_object['remote_server_login_details']
    return {'user_name': configuration_values[0]['remote_user'], 'password': configuration_values[0]['remote_password']}


def get_predefined_input_parameters():
    configuration_object = get_configuration_file()
    configuration_values = configuration_object['input_parameters']
    return configuration_values


def get_email_settings():
    configuration_object = get_configuration_file()
    return configuration_object['email_configurations']


def get_only_predefined_input_parameters():
    configuration_object = get_configuration_file()
    configuration_values = configuration_object['input_parameters']
    parameter_list = []
    for configuration_value in configuration_values:
        parameter_list.append(configuration_value['key'])
    return parameter_list


def get_ldap_configuration_details():
    configuration_object = get_configuration_file()
    configuration_values = configuration_object['ldap_directory_details']
    return configuration_values


def get_sftp_account_deletion_notification_periods():
    configuration_object = get_configuration_file()
    configuration_values = configuration_object['ldap_directory_details']
    return configuration_object['sftp_account_deletion_notification']


def get_expired_account_object():
    account_object = yaml.load(
        open(os.path.dirname(__file__) + '/../auto-generated-files/expiary_dates_auto_generated_do_not_change.yml'),
        yaml.SafeLoader)
    if account_object is None:
        return False
    account_array = account_object['sftpAccounts']
    return account_array
