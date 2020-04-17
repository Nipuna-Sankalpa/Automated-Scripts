from telnetlib import Telnet

from utility.constants import *
from utility.rules_handler import add_rule


def telnet(ip, port, timeout):
    try:
        Telnet(ip, port, int(timeout))
        return True
    except:
        return False


def main():
    print("========== Enter Details of the IP & port you want to monitor ==========")
    while True:
        print("Fields with * are mandatory")
        _domain = input("*Enter Domain: ")
        _port = input("*Enter Port: ")
        _note = input("*Enter Description which should be shown in alert email: ")
        _subject = input("*Enter Notification subject which should be shown in alert email: ")
        status = telnet(_domain, _port, 2)

        if not (_domain == '' or _port == '' or _note == '' or (not status)):
            add_rule({
                'domain': _domain,
                'port': _port,
                'description': _note,
                'notification_subject': _subject,
                'status': alert_status_pass
            })
            break
        else:
            if not status:
                print("Domain and IP is invalid. Connection is not established")
                print("Please enter correct inputs")
            else:
                print("Input Incorrect Please enter correct inputs")


main()
