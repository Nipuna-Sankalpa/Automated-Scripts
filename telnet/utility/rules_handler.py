import os

import yaml


def get_configuration_file():
    with open(os.path.dirname(__file__) + '/settings/rules.yml') as file_path:
        configuration_object = yaml.load(file_path, yaml.SafeLoader)
    return configuration_object


def update_rules_file(file_object):
    file_path = os.path.dirname(__file__) + '/settings/rules.yml'
    try:
        with open(file_path, 'w') as outfile:
            yaml.dump(file_object, outfile, default_flow_style=False)
        return True
    except:
        return False


def add_rule(rule_object):
    rules = get_configuration_file()
    try:
        rules['connection_rules'].append(rule_object)
        update_rules_file(rules)
    except:
        return False
    return True
