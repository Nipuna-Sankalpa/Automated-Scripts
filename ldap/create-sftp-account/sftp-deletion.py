from datetime import date
from datetime import timedelta

from utility.SFTP_deletion_mail import *
from utility.constants import *


def main():
    notification_object = get_sftp_account_deletion_notification_periods()
    notification_time_period = notification_object['time_period']
    sftp_account_array = get_expired_account_object()

    for sftp_account in sftp_account_array:
        accountType = sftp_account['accountType']

        if accountType == account_type_permanent:
            continue

        addedDate = sftp_account['addedDate']
        clientType = sftp_account['clientType']
        requesterEmailAddress = sftp_account['requesterEmailAddress']
        serverIP = sftp_account['serverIP']
        username = sftp_account['username']
        validityPeriod = sftp_account['validityPeriod']

        send_warning_notification(sftp_account)


def send_warning_notification(account_object):
    notification_period = get_sftp_account_deletion_notification_periods()['time_period']
    for period in notification_period:
        delta = int(account_object['validityPeriod']) - int(period)
        should_notified = time_difference(account_object['addedDate'], delta)
        if should_notified:
            account_object['deletionDate'] = date.today() + timedelta(days=int(period))
            send_warning_email(account_object)


def delete_account(sftp_account):
    print('')


def time_difference(added_date, delta):
    date_lexical_terms = added_date.split('-')
    added_date = date(int(date_lexical_terms[0]), int(date_lexical_terms[1]), int(date_lexical_terms[2]))
    today = date.today()
    date_diff = today - added_date

    if date_diff.days >= int(delta):
        return True
    return False
