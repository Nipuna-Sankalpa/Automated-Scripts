from telnetlib import Telnet

from utility.alert_fail import *
from utility.alert_pass import *
from utility.configurations import *
from utility.constants import *
from utility.rules_handler import *


def telnet(ip, port, timeout):
    try:
        Telnet(ip, port, int(timeout))
        return True
    except:
        return False


def main():
    rules_object = get_configuration_file()
    _rules = rules_object['connection_rules']

    for rule in _rules:
        _ip = rule['domain']
        _port = rule['port']
        _note = rule['description']
        email_subject = rule['notification_subject']
        _timeout = 2
        status = telnet(_ip, _port, _timeout)

        if status is False:
            if rule['status'] == alert_status_pass:
                send_fail_email(_ip, _port, _note,email_subject)
                rule['status'] = alert_status_fail
                update_rules_file(rules_object)
        elif status is True:
            if rule['status'] == alert_status_fail:
                send_pass_email(_ip, _port, _note,email_subject)
                rule['status'] = alert_status_pass
                update_rules_file(rules_object)


main()
