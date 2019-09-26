from telnetlib import Telnet

_ip = 'ftp.orangehrm.com'
_port = "389"
_timeout = "2"


def telnet(ip, port, timeout):
    try:
        Telnet(ip, port, int(timeout))
        return True
    except:
        return False


print(telnet(_ip, _port, _timeout))
