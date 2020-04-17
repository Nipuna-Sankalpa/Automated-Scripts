import os

import yaml


def get_configuration_file():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/settings/configurations.yml'), yaml.SafeLoader)
    return configuration_object


def get_email_settings():
    configuration_object = get_configuration_file()
    return configuration_object['email_configurations']


def get_alert_settings():
    configuration_object = get_configuration_file()
    emails = configuration_object['alert_settings']['alert_recipient']
    return emails
