import os
import subprocess
import time

import paramiko

import utility


def create_ftp_home_directory(sftp_username):
    if not os.path.exists("/ftp/" + sftp_username):
        os.makedirs("/ftp/" + sftp_username + "/data")
        subprocess.call(['chmod', '-R', '0755', '/ftp/' + sftp_username])
        subprocess.call(['chown', sftp_username + ':client', '/ftp/' + sftp_username])
        return True
    else:
        return False


def create_remote_home_directory(sftp_user_name, remote_ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    login_details = utility.get_remote_user()
    ssh.connect(remote_ip, port=2112, username=login_details['user_name'], password=login_details['password'])
    shell = ssh.invoke_shell()
    time.sleep(1)
    shell.send("sudo mkdir -p /ftp/" + sftp_user_name + "/data\n")
    print(shell.recv(9999).decode('utf-8'))
    time.sleep(2)
    shell.send(login_details['password'] + "\n")
    time.sleep(10)
    print(shell.recv(9999).decode('utf-8'))
    shell.send("sudo chown {} /ftp/" + sftp_user_name + "/data\n")
    shell.close()
    ssh.close()


create_remote_home_directory('', '')
