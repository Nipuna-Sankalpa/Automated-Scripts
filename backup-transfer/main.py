import pysftp
import os
import yaml
from datetime import datetime, timedelta

sftp_host = "161.47.68.144"
sftp_port = 2112
user_name = "nipuna"
password = "m1Bq0EvDJ@!S"

sabertooth_backup_location = "/var/spool/holland/default/newest/backup_data/"
rogue_backup_root_location = "/sabertooth/backups"
backup_suffix = ".sql.gz"


# this method will clean the old database backup and create workspace for the new backup
def backup_workspace_preparation():
    today = datetime.today().strftime('%Y-%m-%d')
    yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    current_backup_location = rogue_backup_root_location + yesterday
    new_backup_location = rogue_backup_root_location + today
    is_current_backup_exist = os.path.isdir(current_backup_location)
    if is_current_backup_exist:
        with pysftp.Connection(host=sftp_host, username=user_name, password=password, port=sftp_port) as sftp:
            sftp.execute("rm -rf " + current_backup_location)
            sftp.execute("mkdir -p " + new_backup_location)
            sftp.close()

    return {'new_backup_location': new_backup_location}


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
                result['valid_databases'].append(database)
            else:
                result['invalid_databases'].append(database)
    return upload_file(result)


# this method will upload the databases to the new location
def upload_file(databases, backup_location):
    if len(databases['valid_databases']) <= 0:
        return False

    with pysftp.Connection(host=sftp_host, username=user_name, password=password, port=sftp_port) as sftp:
        print("SFTP Connection established")
        for db_name in databases['valid_databases']:
            local_db_path = sabertooth_backup_location + db_name + backup_suffix
            sftp.put(local_db_path, backup_location['new_backup_location'])

        sftp.close()


def main():
    backup_locations = backup_workspace_preparation()
    databases = extract_valid_databases()
    upload_file(databases, backup_locations)


main()
