This project is created to transfer backups from Sabertooth to Rogue
Required packages
pysftp==0.2.8 (Dont install 0.2.9. it has a bug. which leads to login failure)


Rogue backup storing location - /sabertooth/backups
Sabertooth backup location - /var/spool/holland/default/newest/backup_data


#server side SFTP account creation
There will be dedicated sftp account to transfer backup from Sabertooth to Rogue
That account is specifically created for backup transactions and chrooted to its home directory 
