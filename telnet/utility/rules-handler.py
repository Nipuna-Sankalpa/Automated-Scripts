import os

import yaml


def get_configuration_file():
    configuration_object = yaml.load(open(os.path.dirname(__file__) + '/settings/rules.yml'), yaml.SafeLoader)
    return configuration_object


def update_rules_file(file_object):
    with


def add_rule(rule_object):
    rules = get_configuration_file()
    try:
        rules['connection_rules'].append(rule_object)
    except:
        return False
    return True


print(get_configuration_file())
