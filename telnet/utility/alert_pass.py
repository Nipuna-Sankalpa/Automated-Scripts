import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utility.configurations import *


def send_pass_email(domain, port, description, email_subject):
    receiver_email = " ,".join(get_alert_settings())
    message = MIMEMultipart("alternative")
    message["Subject"] = email_subject + " [ ALERT CLOSED ]"
    message["From"] = "server-monitoring@orangehrm.com"
    message["To"] = receiver_email

    # Create the plain-email_body and HTML version of your message
    email_body = """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
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
    <meta content="IE=edge" http-equiv="X-UA-Compatible"/>

</head>
<body>
<div class="">
    <div class="aHl"></div>
    <div id=":bya" tabindex="-1"></div>
    <div id=":bxz" class="ii gt">
        <div id=":bxy" class="a3s aXjCH ">
            <div dir="ltr"><u></u>


                <div style="width:100%;font-family:arial,'helvetica neue',helvetica,sans-serif;padding:0;Margin:0">
                    <div class="m_-8600445106726126258m_-2987716195811134328es-wrapper-color"
                         style="background-color:#f6f6f6">

                        <table class="m_-8600445106726126258m_-2987716195811134328es-wrapper" width="100%"
                               cellspacing="0" cellpadding="0"
                               style="border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top">
                            <tbody>
                            <tr style="border-collapse:collapse">
                                <td valign="top" style="padding:0;Margin:0">
                                    <table class="m_-8600445106726126258m_-2987716195811134328es-content"
                                           cellspacing="0" cellpadding="0" align="center"
                                           style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%">
                                        <tbody>
                                        <tr style="border-collapse:collapse">
                                            <td align="center" style="padding:0;Margin:0">
                                                <table class="m_-8600445106726126258m_-2987716195811134328es-content-body"
                                                       style="border-collapse:collapse;border-spacing:0px;background-color:transparent"
                                                       width="600" cellspacing="0" cellpadding="0" align="center">
                                                    <tbody>
                                                    <tr style="border-collapse:collapse">
                                                        <td align="left"
                                                            style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px">

                                                            <table class="m_-8600445106726126258m_-2987716195811134328es-left"
                                                                   cellspacing="0" cellpadding="0" align="left"
                                                                   style="border-collapse:collapse;border-spacing:0px;float:left">
                                                                <tbody>
                                                                <tr style="border-collapse:collapse">
                                                                    <td class="m_-8600445106726126258m_-2987716195811134328es-m-p0r m_-8600445106726126258m_-2987716195811134328es-m-p20b"
                                                                        width="356" valign="top" align="center"
                                                                        style="padding:0;Margin:0">
                                                                        <table width="100%" cellspacing="0"
                                                                               cellpadding="0"
                                                                               style="border-collapse:collapse;border-spacing:0px">
                                                                            <tbody>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="center"
                                                                                    style="padding:0;Margin:0;display:none"></td>
                                                                            </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                </tbody>
                                                            </table>

                                                            <table cellspacing="0" cellpadding="0" align="right"
                                                                   style="border-collapse:collapse;border-spacing:0px">
                                                                <tbody>
                                                                <tr style="border-collapse:collapse">
                                                                    <td width="184" align="left"
                                                                        style="padding:0;Margin:0">
                                                                        <table width="100%" cellspacing="0"
                                                                               cellpadding="0"
                                                                               style="border-collapse:collapse;border-spacing:0px">
                                                                            <tbody>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="center"
                                                                                    style="padding:0;Margin:0;display:none"></td>
                                                                            </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                    <table class="m_-8600445106726126258m_-2987716195811134328es-content"
                                           cellspacing="0" cellpadding="0" align="center"
                                           style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%">
                                        <tbody>
                                        <tr style="border-collapse:collapse">
                                            <td align="center" style="padding:0;Margin:0">
                                                <table class="m_-8600445106726126258m_-2987716195811134328es-content-body"
                                                       width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff"
                                                       align="center"
                                                       style="border-collapse:collapse;border-spacing:0px;background-color:#ffffff">
                                                    <tbody>
                                                    <tr style="border-collapse:collapse">
                                                        <td align="left" bgcolor="#f0f6ed"
                                                            style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:#f0f6ed">
                                                            <table width="100%" cellspacing="0" cellpadding="0"
                                                                   style="border-collapse:collapse;border-spacing:0px">
                                                                <tbody>
                                                                <tr style="border-collapse:collapse">
                                                                    <td width="560" valign="top" align="center"
                                                                        style="padding:0;Margin:0">
                                                                        <table width="100%" cellspacing="0"
                                                                               cellpadding="0"
                                                                               style="border-collapse:collapse;border-spacing:0px">
                                                                            <tbody>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="center" bgcolor="#97cd7e"
                                                                                    style="padding:0;Margin:0;padding-left:10px;padding-top:15px;padding-bottom:15px">
                                                                                    <h2 style="Margin:0;line-height:29px;font-family:'comic sans ms','marker felt-thin',arial,sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#333333">
                                                                                        <strong>Connection Successfully
                                                                                            Established</strong></h2>
                                                                                </td>
                                                                            </tr>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="left"
                                                                                    style="padding:0;Margin:0;padding-top:20px">
                                                                                    <p style="Margin:0;font-size:14px;font-family:'times new roman',times,baskerville,georgia,serif;line-height:21px;color:#333333">
                                                                                        Hi Team,</p></td>
                                                                            </tr>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="left"
                                                                                    style="padding:0;Margin:0;padding-top:15px">
                                                                                    <p style="Margin:0;font-size:14px;font-family:'times new roman',times,baskerville,georgia,serif;line-height:21px;color:#333333">
                                                                                        This is to let you know that the
                                                                                        following link is now&nbsp;connecting
                                                                                        with the desired service. Alert
                                                                                        closed.</p></td>
                                                                            </tr>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="left"
                                                                                    style="padding:0;Margin:0;padding-top:5px">
                                                                                    <ul>
                                                                                        <li style="font-size:14px;font-family:'courier new',courier,'lucida sans typewriter','lucida typewriter',monospace;line-height:14px;Margin-bottom:15px;color:#333333">
                                                                                            <strong>Domain Name
                                                                                                :</strong>
                                                                                            {{domain_name}}
                                                                                        </li>
                                                                                        <li style="font-size:14px;font-family:'courier new',courier,'lucida sans typewriter','lucida typewriter',monospace;line-height:14px;Margin-bottom:15px;color:#333333">
                                                                                            <strong>Port :</strong>
                                                                                            {{port}}
                                                                                        </li>
                                                                                        <li style="font-size:14px;font-family:'courier new',courier,'lucida sans typewriter','lucida typewriter',monospace;line-height:14px;Margin-bottom:15px;color:#333333">
                                                                                            <strong>Description&nbsp;:</strong>
                                                                                            {{description}}
                                                                                        </li>
                                                                                    </ul>
                                                                                </td>
                                                                            </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                    <table class="m_-8600445106726126258m_-2987716195811134328es-footer" cellspacing="0"
                                           cellpadding="0" align="center"
                                           style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top">
                                        <tbody>
                                        <tr style="border-collapse:collapse">
                                            <td align="center" style="padding:0;Margin:0">
                                                <table class="m_-8600445106726126258m_-2987716195811134328es-footer-body"
                                                       width="600" cellspacing="0" cellpadding="0" align="center"
                                                       style="border-collapse:collapse;border-spacing:0px;background-color:transparent">
                                                    <tbody>
                                                    <tr style="border-collapse:collapse">
                                                        <td align="left"
                                                            style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px">
                                                            <table width="100%" cellspacing="0" cellpadding="0"
                                                                   style="border-collapse:collapse;border-spacing:0px">
                                                                <tbody>
                                                                <tr style="border-collapse:collapse">
                                                                    <td width="560" valign="top" align="center"
                                                                        style="padding:0;Margin:0">
                                                                        <table width="100%" cellspacing="0"
                                                                               cellpadding="0"
                                                                               style="border-collapse:collapse;border-spacing:0px">
                                                                            <tbody>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="center"
                                                                                    style="padding:20px;Margin:0">
                                                                                    <table width="75%" height="100%"
                                                                                           cellspacing="0"
                                                                                           cellpadding="0" border="0"
                                                                                           style="border-collapse:collapse;border-spacing:0px">
                                                                                        <tbody>
                                                                                        <tr style="border-collapse:collapse">
                                                                                            <td style="padding:0;Margin:0px 0px 0px 0px;border-bottom:1px solid #cccccc;background:none;height:1px;width:100%;margin:0px"></td>
                                                                                        </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="center"
                                                                                    style="padding:0;Margin:0;padding-top:10px;padding-bottom:10px">
                                                                                    <p style="Margin:0;font-size:11px;font-family:arial,'helvetica neue',helvetica,sans-serif;line-height:17px;color:#333333">
                                                                                        Techops Server Monitoring
                                                                                        Agent</p>
                                                                                    <p style="Margin:0;font-size:11px;font-family:arial,'helvetica neue',helvetica,sans-serif;line-height:17px;color:#333333">
                                                                                        © 2019 OrangeHRM Inc</p>
                                                                                </td>
                                                                            </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                    <table class="m_-8600445106726126258m_-2987716195811134328es-content"
                                           cellspacing="0" cellpadding="0" align="center"
                                           style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%">
                                        <tbody>
                                        <tr style="border-collapse:collapse">
                                            <td align="center" style="padding:0;Margin:0">
                                                <table class="m_-8600445106726126258m_-2987716195811134328es-content-body"
                                                       style="border-collapse:collapse;border-spacing:0px;background-color:transparent"
                                                       width="600" cellspacing="0" cellpadding="0" align="center">
                                                    <tbody>
                                                    <tr style="border-collapse:collapse">
                                                        <td align="left"
                                                            style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-bottom:30px">
                                                            <table width="100%" cellspacing="0" cellpadding="0"
                                                                   style="border-collapse:collapse;border-spacing:0px">
                                                                <tbody>
                                                                <tr style="border-collapse:collapse">
                                                                    <td width="560" valign="top" align="center"
                                                                        style="padding:0;Margin:0">
                                                                        <table width="100%" cellspacing="0"
                                                                               cellpadding="0"
                                                                               style="border-collapse:collapse;border-spacing:0px">
                                                                            <tbody>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td align="center"
                                                                                    style="padding:0;Margin:0;display:none"></td>
                                                                            </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        <div class="yj6qo"></div>
                        <div class="adL">
                        </div>
                    </div>
                    <div class="adL">
                    </div>
                </div>
                <div class="adL">
                </div>
            </div>
            <div class="adL">
            </div>
        </div>
    </div>
    <div id=":byf" class="ii gt" style="display:none">
        <div id=":bye" class="a3s aXjCH undefined"></div>
    </div>
    <div class="hi"></div>
</div>
</body>
</html>

                """

    email_body = email_body.replace('{{domain_name}}', domain)
    email_body = email_body.replace('{{port}}', port)
    email_body = email_body.replace('{{description}}', description)
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
            "server-monitoring@orangehrm.com", receiver_email.split(","), message.as_string()
        )
