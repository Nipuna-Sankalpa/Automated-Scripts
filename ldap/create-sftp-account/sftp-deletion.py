from datetime import date
from datetime import timedelta

from services.directory_operations import remove_deleted_accounts_from_config_file
from services.ldap_operations import ldap_delete_user, ldap_connect, remove_sftp_account_from_user_groups
from utility.SFTP_deletion_mail import *
from utility.constants import *


def main():
    sftp_account_array = get_expired_account_object()
    for i, sftp_account in enumerate(sftp_account_array):
        account_type = sftp_account['account_type']

        if account_type == account_type_permanent:
            continue
        delete_status = delete_account(sftp_account)
        send_warning_notification(sftp_account)
        if delete_status:
            del sftp_account_array[i]
    remove_deleted_accounts_from_config_file(sftp_account)


def send_warning_notification(account_object):
    notification_period = get_sftp_account_deletion_notification_periods()['time_period']
    for period in notification_period:
        delta = int(account_object['validityPeriod']) - int(period)
        should_notified = time_difference(account_object['addedDate'], delta)
        if should_notified:
            account_object['deletionDate'] = date.today() + timedelta(days=int(period))
            send_warning_email(account_object)


def delete_account(sftp_account):
    account_status = time_difference(sftp_account['addedDate'], sftp_account['validityPeriod'])

    if account_status:
        ldap_configurations_details = get_ldap_configuration_details()
        ldap_host = ldap_configurations_details['ldap_host']
        ldap_port = ldap_configurations_details['ldap_port']
        ldap_bind_user_name = ldap_configurations_details['ldap_bind_user_name']
        ldap_bind_user_password = ldap_configurations_details['ldap_bind_user_password']

        dn = "uid={{user_name}},ou={{account_type}},ou=clients,ou=users,dc=orangehrm,dc=com"
        dn = dn.replace("{{user_name}}", sftp_account['username'])
        dn = dn.replace("{{account_type}}", account_type_temporary)

        ldap_connection = ldap_connect(ldap_host, ldap_port, 'ldaps')
        connection_status = ldap_connection.simple_bind_s(ldap_bind_user_name, ldap_bind_user_password)

        if connection_status:
            ldap_delete_user(ldap_connection, dn)
            remove_sftp_account_from_user_groups(ldap_connection, sftp_account['username'])
            send_deletion_email()
        return True

    return False


def time_difference(added_date, delta):
    date_lexical_terms = added_date.split('-')
    added_date = date(int(date_lexical_terms[0]), int(date_lexical_terms[1]), int(date_lexical_terms[2]))
    today = date.today()
    date_diff = today - added_date

    if date_diff.days == int(delta):
        return True
    return False
