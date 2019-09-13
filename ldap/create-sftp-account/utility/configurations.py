import os

import yaml


def get_remote_user():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'))
    configuration_values = configuration_object['script_configurations']
    return {'user_name': configuration_values[0]['remote_user'], 'password': configuration_values[0]['remote_password']}


def get_input_parameters():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/../configurations.yml'))
    configuration_values = configuration_object['input_parameters']
    return configuration_values
