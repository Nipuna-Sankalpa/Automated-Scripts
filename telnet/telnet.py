from telnetlib import Telnet

_ip = 'ftp.orangehrm.com'
# _ip = '161.47.68.144'
_port = "681237"
_timeout = "5"


def telnet(ip, port, timeout):
    try:
        Telnet(ip, port, int(timeout))
        return True
    except:
        return False


print(telnet(_ip, _port, _timeout))
