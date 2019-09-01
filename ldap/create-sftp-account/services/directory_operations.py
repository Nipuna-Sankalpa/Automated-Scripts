import os
import subprocess


def create_ftp_home_directory(sftp_username):
    if not os.path.exists("/ftp/" + sftp_username):
        os.makedirs("/ftp/" + sftp_username + "/data")
        subprocess.call(['chmod', '-R', '0755', '/ftp/' + sftp_username])
        subprocess.call(['chown', sftp_username + ':client', '/ftp/' + sftp_username])
        return True
    else:
        return False
