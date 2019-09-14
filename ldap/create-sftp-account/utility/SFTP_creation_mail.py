import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utility.configurations import *


def send_email(receiver_email, sftp_user_name, sftp_password, sftp_hostname,
               sftp_port):
    message = MIMEMultipart("alternative")
    message["Subject"] = "[SFTP Account][Client] SFTP Account for " + sftp_user_name.capitalize()
    message["From"] = "webmaster@orangehrm.com"
    message["To"] = receiver_email

    # Create the plain-email_body and HTML version of your message
    email_body = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:v="urn:schemas-microsoft-com:vml">
<head>
    <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml><![endif]-->
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="width=device-width" name="viewport"/>
    <!--[if !mso]><!-->
    <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
    <!--<![endif]-->
    <title></title>
    <!--[if !mso]><!-->
    <!--<![endif]-->
    <style type="text/css">
        body {
            margin: 0;
            padding: 0;
        }

        table,
        td,
        tr {
            vertical-align: top;
            border-collapse: collapse;
        }

        * {
            line-height: inherit;
        }

        a[x-apple-data-detectors=true] {
            color: inherit !important;
            text-decoration: none !important;
        }
    </style>
    <style id="media-query" type="text/css">
        @media (max-width: 615px) {

            .block-grid,
            .col {
                min-width: 320px !important;
                max-width: 100% !important;
                display: block !important;
            }

            .block-grid {
                width: 100% !important;
            }

            .col {
                width: 100% !important;
            }

            .col > div {
                margin: 0 auto;
            }

            img.fullwidth,
            img.fullwidthOnMobile {
                max-width: 100% !important;
            }

            .no-stack .col {
                min-width: 0 !important;
                display: table-cell !important;
            }

            .no-stack.two-up .col {
                width: 50% !important;
            }

            .no-stack .col.num4 {
                width: 33% !important;
            }

            .no-stack .col.num8 {
                width: 66% !important;
            }

            .no-stack .col.num4 {
                width: 33% !important;
            }

            .no-stack .col.num3 {
                width: 25% !important;
            }

            .no-stack .col.num6 {
                width: 50% !important;
            }

            .no-stack .col.num9 {
                width: 75% !important;
            }

            .video-block {
                max-width: none !important;
            }

            .mobile_hide {
                min-height: 0px;
                max-height: 0px;
                max-width: 0px;
                display: none;
                overflow: hidden;
                font-size: 0px;
            }

            .desktop_hide {
                display: block !important;
                max-height: none !important;
            }
        }
    </style>
</head>
<body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #F3F3F3;">
<!--[if IE]>
<div class="ie-browser"><![endif]-->
<table bgcolor="#F3F3F3" cellpadding="0" cellspacing="0" class="nl-container" role="presentation"
       style="table-layout: fixed; vertical-align: top; min-width: 320px; Margin: 0 auto; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #F3F3F3; width: 100%;"
       valign="top" width="100%">
    <tbody>
    <tr style="vertical-align: top;" valign="top">
        <td style="word-break: break-word; vertical-align: top;" valign="top">
            <!--[if (mso)|(IE)]>
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td align="center" style="background-color:#F3F3F3"><![endif]-->
            <div style="background-color:transparent;">
                <div class="block-grid"
                     style="Margin: 0 auto; min-width: 320px; max-width: 595px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #FFE09B;">
                    <div style="border-collapse: collapse;display: table;width: 100%;background-color:#FFE09B;">
                        <!--[if (mso)|(IE)]>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0"
                               style="background-color:transparent;">
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" style="width:595px">
                                        <tr class="layout-full-width" style="background-color:#FFE09B"><![endif]-->
                        <!--[if (mso)|(IE)]>
                        <td align="center" width="595"
                            style="background-color:#FFE09B;width:595px; border-top: 0px solid transparent; border-left: 8px solid #F1F3F3; border-bottom: 0px solid transparent; border-right: 8px solid #F1F3F3;"
                            valign="top">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="padding-right: 50px; padding-left: 50px; padding-top:50px; padding-bottom:5px;background-color:#FFFFFF;">
                        <![endif]-->
                        <div class="col num12"
                             style="min-width: 320px; max-width: 595px; display: table-cell; vertical-align: top; width: 579px;">
                            <div style="background-color:#FFFFFF;width:100% !important;">
                                <!--[if (!mso)&(!IE)]><!-->
                                <div style="border-top:0px solid transparent; border-left:8px solid #F1F3F3; border-bottom:0px solid transparent; border-right:8px solid #F1F3F3; padding-top:50px; padding-bottom:5px; padding-right: 50px; padding-left: 50px;">
                                    <!--<![endif]-->
                                    <!--[if mso]>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tr>
                                            <td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif">
                                    <![endif]-->
                                    <div style="color:#CFCFCF;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;line-height:120%;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                        <div style="font-size: 12px; line-height: 14px; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; color: #CFCFCF;">
                                            <p style="font-size: 14px; line-height: 16px; text-align: left; margin: 0;">
                                                <strong>HELLO,</strong></p>
                                        </div>
                                    </div>
                                    <!--[if mso]></td></tr></table><![endif]-->
                                    <!--[if !mso]><!-->
                                    <div class="desktop_hide"
                                         style="mso-hide: all; display: block; max-height: 0px;">
                                        <!--[if mso]>
                                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif">
                                        <![endif]-->
                                        <div style="color:#66BECD;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;line-height:150%;padding-top:2px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                            <div style="line-height: 18px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; color: #66BECD;">
                                                <p style="line-height: 36px; text-align: left; font-size: 12px; margin: 0;">
                                                    <span style="font-size: 24px;font-weight: bold;">SFTP Account Details - {{user_display_name}}</span>
                                                </p>
                                            </div>
                                        </div>
                                        <!--[if mso]></td></tr></table><![endif]-->
                                    </div>
                                    <!--<![endif]-->
                                    <!--[if (!mso)&(!IE)]><!-->
                                </div>
                                <!--<![endif]-->
                            </div>
                        </div>
                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
            </div>
            <div style="background-color:transparent;">
                <div class="block-grid"
                     style="Margin: 0 auto; min-width: 320px; max-width: 595px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #FFE09B;">
                    <div style="border-collapse: collapse;display: table;width: 100%;background-color:#FFE09B;">
                        <!--[if (mso)|(IE)]>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0"
                               style="background-color:transparent;">
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" style="width:595px">
                                        <tr class="layout-full-width" style="background-color:#FFE09B"><![endif]-->
                        <!--[if (mso)|(IE)]>
                        <td align="center" width="595"
                            style="background-color:#FFE09B;width:595px; border-top: 0px solid transparent; border-left: 8px solid #F1F3F3; border-bottom: 0px solid transparent; border-right: 8px solid #F1F3F3;"
                            valign="top">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="padding-right: 0px; padding-left: 0px; padding-top:25px; padding-bottom:0px;background-color:#FFFFFF;">
                        <![endif]-->
                        <div class="col num12"
                             style="min-width: 320px; max-width: 595px; display: table-cell; vertical-align: top; width: 579px;">
                            <div style="background-color:#FFFFFF;width:100% !important;">
                                <!--[if (!mso)&(!IE)]><!-->
                                <div style="border-top:0px solid transparent; border-left:8px solid #F1F3F3; border-bottom:0px solid transparent; border-right:8px solid #F1F3F3; padding-top:25px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;">
                                    <!--<![endif]-->
                                    <div align="center" class="img-container center autowidth fullwidth"
                                         style="padding-right: 0px;padding-left: 0px;">
                                        <!--[if mso]>
                                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                            <tr style="line-height:0px">
                                                <td style="padding-right: 0px;padding-left: 0px;" align="center">
                                        <![endif]-->
                                        <div style="font-size:1px;line-height:10px"> </div>
                                        <img title="Image" width="579" alt="divider.png" align="center" alt="Image"
                                             border="0" class="center autowidth fullwidth"
                                             style="text-decoration: none; -ms-interpolation-mode: bicubic; border: 0; height: auto; width: 100%; max-width: 579px; display: block;"
                                             src="https://drive.google.com/uc?export=view&id=1bBNKQraslaEoE2utEzmEnKkDINL17R-1"/>
                                        <!--[if mso]></td></tr></table><![endif]-->
                                    </div>
                                    <!--[if (!mso)&(!IE)]><!-->
                                </div>
                                <!--<![endif]-->
                            </div>
                        </div>
                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
            </div>
            <div style="background-color:transparent;">
                <div class="block-grid"
                     style="Margin: 0 auto; min-width: 320px; max-width: 595px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #FFE09B;">
                    <div style="border-collapse: collapse;display: table;width: 100%;background-color:#FFE09B;">
                        <!--[if (mso)|(IE)]>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0"
                               style="background-color:transparent;">
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" style="width:595px">
                                        <tr class="layout-full-width" style="background-color:#FFE09B"><![endif]-->
                        <!--[if (mso)|(IE)]>
                        <td align="center" width="595"
                            style="background-color:#FFE09B;width:595px; border-top: 0px solid transparent; border-left: 8px solid #F1F3F3; border-bottom: 0px solid transparent; border-right: 8px solid #F1F3F3;"
                            valign="top">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="padding-right: 50px; padding-left: 50px; padding-top:35px; padding-bottom:5px;background-color:#FFFFFF;">
                        <![endif]-->
                        <div class="col num12"
                             style="min-width: 320px; max-width: 595px; display: table-cell; vertical-align: top; width: 579px;">
                            <div style="background-color:#FFFFFF;width:100% !important;">
                                <!--[if (!mso)&(!IE)]><!-->
                                <div style="border-top:0px solid transparent; border-left:8px solid #F1F3F3; border-bottom:0px solid transparent; border-right:8px solid #F1F3F3; padding-top:0px; padding-bottom:5px; padding-right: 50px; padding-left: 50px;">
                                    <!--<![endif]-->
                                    <!--[if mso]>
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tr>
                                            <td style="padding-right: 10px; padding-left: 10px; padding-top: 15px; padding-bottom: 10px; font-family: Arial, sans-serif">
                                    <![endif]-->
                                    <div style="color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;line-height:150%;padding-top:15px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                        <div style="font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; line-height: 18px; color: #555555;">
                                            <p style="font-size: 12px; line-height: 24px; margin: 0;"><span
                                                    style="font-size: 16px;">Hi Team,<strong><br/></strong>Please find the following SFTP details for {{user_display_name}}.</span>
                                            </p>
                                            <ul>
                                                <li style="font-size: 12px; line-height: 18px;"><span
                                                        style="font-size: 16px; line-height: 24px;"><strong>Username</strong> : {{user_name}}</span>
                                                </li>
                                                <li style="font-size: 12px; line-height: 18px;"><span
                                                        style="font-size: 16px; line-height: 24px;"><strong>Password</strong> : {{password}}</span>
                                                </li>
                                                <li style="font-size: 12px; line-height: 18px;"><span
                                                        style="font-size: 16px; line-height: 24px;"><strong>Protocol</strong> : SFTP</span>
                                                </li>
                                                <li style="font-size: 12px; line-height: 18px;"><span
                                                        style="font-size: 16px; line-height: 24px;"><strong>Location</strong> : /data</span>
                                                </li>
                                                <li style="font-size: 12px; line-height: 18px;"><span
                                                        style="font-size: 16px; line-height: 24px;"><strong>Host</strong> : {{hostname}}</span>
                                                </li>
                                                <li style="font-size: 12px; line-height: 18px;"><span
                                                        style="font-size: 16px; line-height: 24px;"><strong>Port</strong> : 2112</span>
                                                </li>
                                            </ul>
                                        </div>
                                        <div style="font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; line-height: 18px; color: #555555;">
                                            <p style="font-size: 0px;line-height: 14px;margin-top: 34px;"><span
                                                    style="font-size: 14px;font-family: serif;"><strong>Note:</strong> This is an automated email. if you have any concerns, please contact <strong><i>Techops</i></strong></span>
                                            </p>
                                        </div>
                                    </div>
                                    <!--[if mso]></td></tr></table><![endif]-->
                                    <!--[if (!mso)&(!IE)]><!-->
                                </div>
                                <!--<![endif]-->
                            </div>
                        </div>
                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                    </div>
                </div>
            </div>
            <div style="background-color:transparent;">
                <div class="block-grid"
                     style="Margin: 0 auto; min-width: 320px; max-width: 595px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word;">
                    <div style="border-collapse: collapse;margin-left:8px;display: table;width: 100%;">
                        <!--[if (mso)|(IE)]>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0"
                               style="background-color:transparent;">
                            <tr>
                                <td align="center">
                                    <table cellpadding="0" cellspacing="0" border="0" style="width:595px">
                                        <tr class="layout-full-width" style="background-color:#FFE09B"><![endif]-->
                        <!--[if (mso)|(IE)]>
                        <td align="center" width="595"
                            style="background-color:#FFE09B;width:595px; border-top: 0px solid transparent; border-left: 8px solid #F1F3F3; border-bottom: 0px solid transparent; border-right: 8px solid #F1F3F3;"
                            valign="top">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="padding-right: 0px; padding-left: 0px; padding-top:30px; padding-bottom:25px;">
                        <![endif]-->
                        <div class="col num12"
                             style="min-width: 320px; max-width: 595px; display: table-cell; vertical-align: top; width: 579px;">
                            <div style="width:100% !important;">
                                <img alt="SFTP_MAIL_FOOTER.png"
                                     src="https://drive.google.com/uc?export=view&id=1gmLGsWRALiOtcXaSIONMKmvAt91rkz7H"/>
                            </div>
                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                        </div>
                    </div>
                </div>
                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
    </tr>
    </tbody>
</table>
<!--[if (IE)]></div><![endif]-->
</body>
</html>

            """

    email_body = email_body.replace('{{user_display_name}}', sftp_user_name.capitalize())
    email_body = email_body.replace('{{user_name}}', sftp_user_name)
    email_body = email_body.replace('{{password}}', sftp_password)
    email_body = email_body.replace('{{hostname}}', sftp_hostname)
    email_body = email_body.replace('{{port}}', sftp_port)
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(email_body, "html")

    # Add HTML/plain-email_body parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    email_settings_object = get_email_settings()
    # Create secure# e connection with server and send email
    context = ssl.create_default_context()

    with smtplib.SMTP(email_settings_object['host'], email_settings_object['port']) as server:
        server.starttls(context=context)  # Secure the connection
        server.login(email_settings_object['user_name'], email_settings_object['password'])
        server.sendmail(
            "ldap-admin@orangehrm.com", receiver_email, message.as_string()
        )
