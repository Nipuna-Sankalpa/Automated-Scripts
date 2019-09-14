import os
import subprocess
import time

import paramiko
import yaml

from utility.configurations import get_remote_user


def create_sftp_home_directory(sftp_username):
    if not os.path.exists("/ftp/" + sftp_username):
        os.makedirs("/ftp/" + sftp_username + "/data")
        subprocess.call(['chmod', '-R', '0700', '/ftp/' + sftp_username + '/data'])
        subprocess.call(['chmod', '-R', '0755', '/ftp/' + sftp_username])
        subprocess.call(['chown', sftp_username + ':client', '/ftp/' + sftp_username + "/data"])
        return True
    else:
        return False


def create_remote_sftp_home_directory(sftp_user_name, remote_ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    login_details = get_remote_user()
    ssh.connect(remote_ip, port=2112, username=login_details['user_name'], password=login_details['password'])
    shell = ssh.invoke_shell()
    time.sleep(1)
    shell.send("sudo mkdir -p /ftp/" + sftp_user_name + "/data\n")
    print(shell.recv(9999).decode('utf-8'))
    time.sleep(2)
    shell.send(login_details['password'] + "\n")
    time.sleep(3)
    print(shell.recv(9999).decode('utf-8'))
    shell.send("sudo chown " + sftp_user_name + ":client /ftp/" + sftp_user_name + "/data\n")
    shell.send(login_details['password'] + "\n")
    time.sleep(3)
    shell.send("sudo chmod 700 /ftp/" + sftp_user_name + "/data\n")
    shell.send(login_details['password'] + "\n")
    time.sleep(3)
    shell.send("sudo chmod 755 /ftp/" + sftp_user_name)
    shell.send(login_details['password'] + "\n")
    time.sleep(3)
    shell.close()
    ssh.close()


def update_expire_dates_file(user_account_object):
    file_path = os.path.dirname(__file__) + "/../auto-generated-files/expiary_dates_auto_generated_do_not_change.yml"
    with open(file_path) as readfile:
        yaml_input = yaml.load(readfile, yaml.SafeLoader)
    if yaml_input == None:
        yaml_input = {}
        yaml_input['sftpAccounts'] = []

    yaml_input['sftpAccounts'].append(user_account_object)
    with open(file_path, 'w') as outfile:
        yaml.dump(yaml_input, outfile, default_flow_style=False)
