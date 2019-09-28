import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "[Open-Source][Marketplace] Error Log Updated"
    message["From"] = "webmaster@orangehrm.com"
    message["To"] = ",".join(receiver_email)
    message["Cc"] = "XXXXX"

    # Create the plain-email_body and HTML version of your message
    email_body = """\
<div id=":195" class="a3s aXjCH "><u></u>


    <div>
        <div id="m_9032942410317627899:bxz" class="m_9032942410317627899ii m_9032942410317627899gt">
            <div id="m_9032942410317627899:bxy" class="m_9032942410317627899a3s m_9032942410317627899aXjCH">
                <div dir="ltr"><u></u>


                    <div style="width:100%;font-family:arial,'helvetica neue',helvetica,sans-serif;padding:0;Margin:0">
                        <div class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-wrapper-color"
                             style="background-color:#f6f6f6">

                            <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-wrapper"
                                   width="100%" cellspacing="0" cellpadding="0"
                                   style="border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top">
                                <tbody>
                                <tr style="border-collapse:collapse">
                                    <td valign="top" style="padding:0;Margin:0">
                                        <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-content"
                                               cellspacing="0" cellpadding="0" align="center"
                                               style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%">
                                            <tbody>
                                            <tr style="border-collapse:collapse">
                                                <td align="center" style="padding:0;Margin:0">
                                                    <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-content-body"
                                                           style="border-collapse:collapse;border-spacing:0px;background-color:transparent"
                                                           width="600" cellspacing="0" cellpadding="0" align="center">
                                                        <tbody>
                                                        <tr style="border-collapse:collapse">
                                                            <td align="left"
                                                                style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px">

                                                                <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-left"
                                                                       cellspacing="0" cellpadding="0" align="left"
                                                                       style="border-collapse:collapse;border-spacing:0px;float:left">
                                                                    <tbody>
                                                                    <tr style="border-collapse:collapse">
                                                                        <td class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-m-p0r m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-m-p20b"
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
                                        <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-content"
                                               cellspacing="0" cellpadding="0" align="center"
                                               style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%">
                                            <tbody>
                                            <tr style="border-collapse:collapse">
                                                <td align="center" style="padding:0;Margin:0">
                                                    <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-content-body"
                                                           width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff"
                                                           align="center"
                                                           style="border-collapse:collapse;border-spacing:0px;background-color:#ffffff">
                                                        <tbody>
                                                        <tr style="border-collapse:collapse">
                                                            <td align="left" bgcolor="#f6eded"
                                                                style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:#f6eded">
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
                                                                                    <td align="center" bgcolor="#cb6966"
                                                                                        style="padding:0;Margin:0;padding-left:10px;padding-top:15px;padding-bottom:15px">
                                                                                        <h2 style="Margin:0;line-height:29px;font-family:'comic sans ms','marker felt-thin',arial,sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#333333">
                                                                                            <strong>Attention - Error
                                                                                                Log Updated !!!</strong>
                                                                                        </h2></td>
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
                                                                                            This is to let you know that
                                                                                            the
                                                                                            following log file is
                                                                                            updated and it is possible
                                                                                            that Market place is not
                                                                                            functioning at the
                                                                                            moment.</p></td>
                                                                                </tr>
                                                                                <tr style="border-collapse:collapse">
                                                                                    <td align="left"
                                                                                        style="padding:0;Margin:0;padding-top:5px">
                                                                                        <ul>
                                                                                            <br />
                                                                                            <li style="font-size:14px;font-family:'courier new',courier,'lucida sans typewriter','lucida typewriter',monospace;line-height:14px;Margin-bottom:15px;color:#333333">
                                                                                                <strong>Log file
                                                                                                    location:</strong>
                                                                                                marketplace.orangehrm.com/var/log/prod.log
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
                                        <div>
                                            <div class="adm">
                                                <div id="q_40" class="ajR h4">
                                                    <div class="ajT"></div>
                                                </div>
                                            </div>
                                            <div class="h5">
                                                <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-footer"
                                                       cellspacing="0" cellpadding="0" align="center"
                                                       style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top">
                                                    <tbody>
                                                    <tr style="border-collapse:collapse">
                                                        <td align="center" style="padding:0;Margin:0">
                                                            <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-footer-body"
                                                                   width="600" cellspacing="0" cellpadding="0"
                                                                   align="center"
                                                                   style="border-collapse:collapse;border-spacing:0px;background-color:transparent">
                                                                <tbody>
                                                                <tr style="border-collapse:collapse">
                                                                    <td align="left"
                                                                        style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px">
                                                                        <table width="100%" cellspacing="0"
                                                                               cellpadding="0"
                                                                               style="border-collapse:collapse;border-spacing:0px">
                                                                            <tbody>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td width="560" valign="top"
                                                                                    align="center"
                                                                                    style="padding:0;Margin:0">
                                                                                    <table width="100%" cellspacing="0"
                                                                                           cellpadding="0"
                                                                                           style="border-collapse:collapse;border-spacing:0px">
                                                                                        <tbody>
                                                                                        <tr style="border-collapse:collapse">
                                                                                            <td align="center"
                                                                                                style="padding:20px;Margin:0">
                                                                                                <table width="75%"
                                                                                                       height="100%"
                                                                                                       cellspacing="0"
                                                                                                       cellpadding="0"
                                                                                                       border="0"
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
                                                                                                    Techops Server
                                                                                                    Monitoring Agent</p>
                                                                                                <p style="Margin:0;font-size:11px;font-family:arial,'helvetica neue',helvetica,sans-serif;line-height:17px;color:#333333">
                                                                                                    &copy; 2019 OrangeHRM
                                                                                                    Inc</p></td>
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
                                                <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-content"
                                                       cellspacing="0" cellpadding="0" align="center"
                                                       style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%">
                                                    <tbody>
                                                    <tr style="border-collapse:collapse">
                                                        <td align="center" style="padding:0;Margin:0">
                                                            <table class="m_9032942410317627899m_-6020083921654393130m_-6559841846176593223es-content-body"
                                                                   style="border-collapse:collapse;border-spacing:0px;background-color:transparent"
                                                                   width="600" cellspacing="0" cellpadding="0"
                                                                   align="center">
                                                                <tbody>
                                                                <tr style="border-collapse:collapse">
                                                                    <td align="left"
                                                                        style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-bottom:30px">
                                                                        <table width="100%" cellspacing="0"
                                                                               cellpadding="0"
                                                                               style="border-collapse:collapse;border-spacing:0px">
                                                                            <tbody>
                                                                            <tr style="border-collapse:collapse">
                                                                                <td width="560" valign="top"
                                                                                    align="center"
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
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            <div class="yj6qo"></div>
                            <div class="adL">
                            </div>
                            <div class="m_9032942410317627899yj6qo adL"></div>
                            <div class="adL">
                            </div>
                            <div class="m_9032942410317627899adL adL">
                            </div>
                            <div class="adL">
                            </div>
                        </div>
                        <div class="adL">
                        </div>
                        <div class="m_9032942410317627899adL adL">
                        </div>
                        <div class="adL">
                        </div>
                    </div>
                    <div class="adL">
                    </div>
                    <div class="m_9032942410317627899adL adL">
                    </div>
                    <div class="adL">
                    </div>
                </div>
                <div class="adL">
                </div>
                <div class="m_9032942410317627899adL adL">
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
    <div class="adL">


    </div>
</div>
            """

    part1 = MIMEText(email_body, "html")

    message.attach(part1)
    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', '587') as server:
        server.starttls(context=context)  # Secure the connection
        server.login('XXXXX', 'XXXXXX')
        server.sendmail(
            "webmaster@orangehrm.com", receiver_email, message.as_string()
        )


def mail():
    file_path = "abc.txt"
    temp_file_path = "md5checksum.txt"
    output = os.popen('md5sum ' + file_path).read()
    current_md5value = str(output).split(' ')[0]
    if not (os.path.exists(file_path)) or not (os.path.exists(temp_file_path)):
        send_email([])
        return

    with open(temp_file_path, 'r') as file:
        old_md5value = file.read()

    if old_md5value != current_md5value:
        send_email([])
        update_file(temp_file_path, current_md5value)


def update_file(temp_file_path, current_md5value):
    with open(temp_file_path, 'w') as file:
        file.write(current_md5value)


def read_file(temp_file_path):
    with open(temp_file_path, 'r') as file:
        return file.read()


mail()
