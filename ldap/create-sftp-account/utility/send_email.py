import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(email_user_name, password, receiver_email, sftp_user_name, sftp_password, sftp_hostname,
               sftp_port):
    message = MIMEMultipart("alternative")
    message["Subject"] = "[SFTP Account][Client] SFTP Account for " + sftp_user_name.capitalize()
    message["From"] = "webmaster@orangehrm.com"
    message["To"] = receiver_email

    # Create the plain-email_body and HTML version of your message
    email_body = """\
<p>Hi Team,&nbsp;<br />Please find the following SFTP details for Alican.</p>
<ul>
<li><strong>Username</strong> <strong>:</strong>&nbsp; &nbsp; {{username}}</li>
<li><strong>Password</strong> <strong>:</strong>&nbsp; &nbsp; {{password}}</li>
<li><strong>Protocol</strong>&nbsp;&nbsp;<strong>:</strong>&nbsp; &nbsp; &nbsp;SFTP</li>
<li><strong>Location</strong> <strong>:</strong>&nbsp; &nbsp; &nbsp; /data</li>
<li><strong>URL</strong> <strong>:</strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{{hostname}}</li>
<li><strong>Port</strong> <strong>:</strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{{port}}</li>
</ul>
<p>Regards,&nbsp;<br />Techops</p>
            """

    email_body = email_body.replace('{{capitalized_username}}', sftp_user_name.capitalize())
    email_body = email_body.replace('{{username}}', sftp_user_name)
    email_body = email_body.replace('{{password}}', sftp_password)
    email_body = email_body.replace('{{hostname}}', sftp_hostname)
    email_body = email_body.replace('{{port}}', sftp_port)
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(email_body, "html")

    # Add HTML/plain-email_body parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_user_name, password)
        server.sendmail(
            "webmaster@orangehrm.com", receiver_email, message.as_string()
        )


send_email("nipuna499@gmail.com", "", "nipuna@orangehrmlive.com", "nipuna", "nipuna1234", "lcoalhost",
           "2112")
