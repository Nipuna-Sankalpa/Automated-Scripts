import os
from datetime import datetime


def update_sftp_deletion_log():
    print()


def update_sftp_creation_log(input_object):
    timestamp = str(datetime.now())
    created_by = str(os.getlogin())
    log_record = timestamp + ' ' + input_object['username'] + ' ' + input_object['serverIP'] + ' ' + created_by + ' ' + \
                 input_object['requesterEmailAddress']
    log_file_name = os.path.dirname(__file__) + '/../logs/create-sftp.log'
    os.system('echo "' + log_record + '" >> ' + log_file_name)


def update_sftp_deletion_log(input_object):
    timestamp = str(datetime.now())
    log_record = timestamp + ' ' + input_object['username'] + ' ' + input_object['serverIP'] + ' deleted'
    log_file_name = os.path.dirname(__file__) + '/../logs/sftp-deletion.log'
    os.system('echo "' + log_record + '" >> ' + log_file_name)
