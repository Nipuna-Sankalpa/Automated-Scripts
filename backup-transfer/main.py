import pysftp
import os
import subprocess
import yaml
from datetime import datetime, timedelta
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sftp_host = "xxxx"
sftp_port = 1234
user_name = "xxxx"
password = "xxxxx"

sabertooth_backup_location = "/var/spool/holland/default/newest/backup_data/"
rogue_backup_root_location = "/sabertooth/backups/data/"
backup_suffix = ".sql.gz"

# Email Settings
SMTP_SERVER = ""
SMTP_PORT = ""
SMTP_USER_NAME = ""
SMTP_PASSWORD = ""

# Email notification settings
NOTIFICATION_RECEIVER = "techops@orangehrm.com"
NOTIFICATION_SENDER = "server-admin@orangehrm.com"


# log all the errors
def error_log(content):
    pointer = open('error.log', 'a')
    current_date = datetime.today().strftime('%Y-%m-%d')
    pointer.write(current_date + " - " + content + "\n")
    pointer.close()


# this method will clean the old database backup and create workspace for the new backup
def backup_workspace_preparation():
    today = datetime.today().strftime('%Y-%m-%d')
    yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    current_backup_location = rogue_backup_root_location + yesterday
    new_backup_location = rogue_backup_root_location + today
    with pysftp.Connection(host=sftp_host, username=user_name, password=password, port=sftp_port) as sftp:
        sftp.execute("rm -rf " + current_backup_location)
        sftp.execute("mkdir -p " + new_backup_location)
        sftp.close()

    return {'new_backup_location': new_backup_location}


# this function will check for the hash values
def check_integrity_file(file_path, backup_file_type):
    if backup_file_type == "local":
        temp = subprocess.check_output("sha256sum " + file_path, shell=True)
        temp = temp.decode('utf-8')
        return temp.split(' ')[0]
    elif backup_file_type == "remote":
        temp_dictionary = {}
        with pysftp.Connection(host=sftp_host, username=user_name, password=password, port=sftp_port) as sftp:
            command = "cd " + file_path + " && ls | xargs sha256sum"
            result = sftp.execute(command)
            for record in result:
                temp = record.decode('utf-8').split(' ')
                temp_dictionary[temp[2].replace("\n", '')] = temp[0]
            sftp.close()
        return temp_dictionary
    return False


# this method will identify valid databases to be pushed
def extract_valid_databases():
    result = {'invalid_databases': [], 'valid_databases': []}
    with open("database_registry.yml", "r") as database_registry:
        database_list = yaml.load(database_registry, yaml.SafeLoader)
        if len(database_list['databases']) < 0:
            return False

        for database in database_list['databases']:
            db_path = sabertooth_backup_location + database + backup_suffix
            if os.path.exists(db_path):
                db = {
                    'db_name': database,
                    'local_hash_value': check_integrity_file(db_path, "local")
                }
                result['valid_databases'].append(db)
            else:
                result['invalid_databases'].append(database)
    return result


# this method will upload the databases to the remote location location
def upload_file(databases, backup_location):
    if len(databases['valid_databases']) <= 0:
        return False

    with pysftp.Connection(host=sftp_host, username=user_name, password=password, port=sftp_port) as sftp:
        for db_record in databases['valid_databases']:
            local_db_path = sabertooth_backup_location + db_record['db_name'] + backup_suffix
            remote_db_path = backup_location['new_backup_location'] + "/" + db_record['db_name'] + backup_suffix
            sftp.put(local_db_path, remote_db_path)
            print("- Database Name: " + db_record['db_name'] + " -> Status : Uploaded")
            error_log(db_record['db_name'] + " -> Status : Uploaded")

        sftp.close()


# backup post verification
# First check whether backup exists in the remote server. then will be checked for their hash values

def backup_post_verification(databases, backup_locations):
    valid_db_list = databases['valid_databases']
    new_backup_location = backup_locations['new_backup_location']
    failed_dbs = []
    if len(valid_db_list) <= 0:
        error_log("no valid databases available")
        return False

    with pysftp.Connection(host=sftp_host, username=user_name, password=password, port=sftp_port) as sftp:
        uploaded_list = sftp.listdir(new_backup_location)
        for db_record in valid_db_list:
            db_name = db_record['db_name']
            full_backup_db_name = db_name + backup_suffix
            remote_hash_values = check_integrity_file(new_backup_location, 'remote')
            if full_backup_db_name in uploaded_list and db_record['local_hash_value'] == remote_hash_values[
                full_backup_db_name]:
                continue
            else:
                failed_dbs.append(db_name)
        sftp.close()
    if len(failed_dbs) > 0:
        error_log("Following databases have failed to upload " + failed_dbs)
    return failed_dbs


# this function will send status email
def send_status_email(valid_databases, failed_databases):
    registered_databases_count = len(valid_databases['valid_databases'])
    invalid_db_count = len(valid_databases['invalid_databases'])
    failed_upload_count = len(failed_databases)
    current_date = datetime.today().strftime('%Y-%m-%d')
    passed_db_count = registered_databases_count -(invalid_db_count + failed_upload_count)

    message = MIMEMultipart("alternative")

    if failed_upload_count > 0:
        subject = "[Sabertooth][Backup Transfer][Fail] Data Transfer Summary on " + current_date
    else:
        subject = "[Sabertooth][Backup Transfer][Success] Data Transfer Summary on " + current_date

    message["Subject"] = subject
    message["From"] = NOTIFICATION_SENDER
    message["To"] = NOTIFICATION_RECEIVER

    # Create the plain-email_body and HTML version of your message
    file_pointer = open("email_template.html", "r")

    email_body = file_pointer.read()
    file_pointer.close()

    email_body = email_body.replace('#current_date#', current_date)
    email_body = email_body.replace('#failed_db_count#', str(failed_upload_count))
    email_body = email_body.replace('#invalid_db_count#', str(invalid_db_count))
    email_body = email_body.replace('#registered_db_count#', str(registered_databases_count))
    email_body = email_body.replace('#passed_db_count#', str(passed_db_count))
    # Turn these into plain/html MIMEText objects
    part = MIMEText(email_body, "html")

    # Add HTML/plain-email_body parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)
    # Create secure# e connection with server and send email
    context = ssl.create_default_context()

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)  # Secure the connection
        server.login(SMTP_USER_NAME, SMTP_PASSWORD)
        server.sendmail(
            message["From"], message["To"], message.as_string()
        )


# this function will execute all the individual functions
def main():
    backup_locations = backup_workspace_preparation()
    databases = extract_valid_databases()
    upload_file(databases, backup_locations)
    failed_databases = backup_post_verification(databases, backup_locations)
    send_status_email(databases, failed_databases)


main()
