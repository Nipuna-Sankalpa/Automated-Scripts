This project is created to transfer backups from Sabertooth to Rogue
Required packages
pip3 install pysftp==0.2.8 (Dont install 0.2.9. it has a bug. which leads to login failure)
pip3 install email
pip3 install pyaml
pip3 install elasticsearch

Rogue backup storing location - /sabertooth/backups
Sabertooth backup location - /var/spool/holland/default/newest/backup_data

Note : make sure that you add a forward slash at the end of the each backup location. otherwise it will lead to errors

#server side SFTP account creation
There will be dedicated sftp account to transfer backup from Sabertooth to Rogue
That account is specifically created for backup transactions and chrooted to its home directory 

FAQ - 
when installing email module in python, if an error occurs like CSstringIO is missing, then just leave the module installation.
