import requests, json, logging, importlib, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

reset_reference_rules = importlib.import_module('reset-reference-rules')

records_per_page = 50
headers = {
    'Api-Key': 'xxxx'
}


def get_condition_array():
    api_endpoint = "https://infra-api.newrelic.com/v2/alerts/conditions"
    final_response = []
    offset = 0
    get_parameters = {
        'offset': str(offset),
        'list': '50'
    }
    while True:
        response = requests.get(api_endpoint, get_parameters, headers=headers)
        if len(response.json()['data']) > 0:
            final_response = final_response + response.json()['data']
            offset = offset + records_per_page
            get_parameters['offset'] = str(offset)
        else:
            break
    return final_response


def get_synthetic_monitors():
    api_endpoint = "https://synthetics.newrelic.com/synthetics/api/v3/monitors"
    response = requests.get(api_endpoint, headers=headers)
    condition_array = response.json()['monitors']
    return condition_array


def send_email_alert(email_alert):
    smtp_server = "xxx"
    smtp_port = "587"
    username = "xxx"
    password = "xxx"
    message = MIMEMultipart("alternative")
    message["Subject"] = "[New Relic Alerts] New Relic monitoring rules have been modified"
    message["From"] = "New Relic <newrelic-admin@orangehrm.com>"
    message["To"] = 'nipuna@orangehrmlive.com'

    body = """\
<html>
<div id="main" style="width:500px">
<div id="email content">
<p>
Hi Team,<br /><br />

This to let you know that New Relic policies have been modified. <br />
Please refer to the <strong>Error Log Path</strong> for more details.<br /><br />

<strong>Note:</strong> If modifications are legitimate, first fix the issue then reset the reference New Relic rules set. <br />
</p>
</div>
<div style="border-left:1px solid rgb(226,226,226);border-right:1px solid rgb(226,226,226)">
<div style="border-top:5px solid rgb(166,191,128)"></div>
    <table style="width:100%;border-collapse:collapse;border-spacing:0;color:rgb(84,84,84);font-size:14px">
        <tbody>
        <tr>
            <td style="padding-top:25px;padding-bottom:25px;padding-left:25px;padding-right:25px"><img
                    src="https://drive.google.com/uc?export=view&id=1pgoNE-YeJR35WXcMeOOy5IcOLhu20NkB"
                    width="90" height="16" alt="New Relic" data-image-whitelisted="" class="CToWUd"></td>
        </tr>
        <tr>
            <td style="padding-top:0;padding-bottom:25px;padding-left:25px;padding-right:25px">
                <div>
                    <div><a href="https://www.orangehrm.com" style="text-decoration:none;color:rgb(75,143,171)" target="_blank"><span>Triggered by Techops @ OrangeHRM</span></a>
                    </div>
                </div>
            </td>
        </tr>
        </tbody>
    </table>
    <div style="border-top:1px solid rgb(228,228,228)"></div>
    <div style="border-top:1px solid rgb(233,233,233)"></div>
    <div style="border-top:1px solid rgb(239,239,239)"></div>
    <div style="border-top:1px solid rgb(244,244,244)"></div>


</div>

</div>
</html>
"""
    email_body = MIMEText(body, "html")
    message.attach(email_body)

    if email_alert:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(username, password)
            server.sendmail(message["From"], message["To"], message.as_string())


def verify():
    email_alert = False
    logging.basicConfig(filename='error.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
    condition_array = get_condition_array()
    current_infra_rule_id_set = []
    deleted_rules_id = []
    current_synthetic_rule_id_set = []
    exclude_verify_filter = ['created_at_epoch_millis', 'updated_at_epoch_millis', 'violation_close_timer']
    with open("infrastructure-rules.json", 'r') as configuration_file:
        reference_infra_object_array = json.load(configuration_file)

    # verify infrastructure rules
    for element in condition_array:
        current_infra_rule_id_set.append((element['id']))
        key_set = element.keys()
        for key in key_set:
            if key not in exclude_verify_filter:
                reference_object = reference_infra_object_array[str(element['id'])]
                if not (reference_object[key] == element[key]):
                    email_alert = True
                    error_msg = element['name'] + ' : ' + key + ' has been changed'
                    logging.error(error_msg)
                    logging.error("reference object :" + json.dumps(reference_object[key]))
                    logging.error("current object :" + json.dumps(element[key]))

    # verify synthetic monitors rules
    with open("synthetic-rules.json", 'r') as configuration_file:
        reference_synthetic_object_array = json.load(configuration_file)

    synthetic_monitor_array = get_synthetic_monitors()
    for element in synthetic_monitor_array:
        current_synthetic_rule_id_set.append(element['id'])
        if element['status'] == 'DISABLED':
            email_alert = True
            error_msg = element['name'] + ' has been changed'
            logging.error(error_msg)

    # verify whether rules have been added or rules have been deleted from the new relic portal
    current_infrastructure_rule_count = len(condition_array)
    reference_infrastructure_rule_count = len(reference_infra_object_array)

    # infrastructure rule verification
    if reference_infrastructure_rule_count > current_infrastructure_rule_count:
        reference_rule_id_set = reference_infra_object_array.keys()
        deleted_rules_id = reference_rule_id_set - current_infra_rule_id_set
        for x in reference_rule_id_set:
            if x not in current_infra_rule_id_set:
                deleted_rules_id.append(x)
                break
        logging.error("Following Infrastructure conditions have deleted : " + str(deleted_rules_id))
        email_alert = True
    elif reference_infrastructure_rule_count < current_infrastructure_rule_count:
        reset_reference_rules.reset_infrastructure_configurations()

    # synthetic rule verification
    current_synthetic_rule_count = len(synthetic_monitor_array)
    reference_synthetic_rule_count = len(reference_synthetic_object_array)

    if reference_synthetic_rule_count > current_synthetic_rule_count:
        deleted_rules_id = []
        reference_rule_id_set = reference_synthetic_object_array.keys()
        for x in reference_rule_id_set:
            if x not in current_synthetic_rule_id_set:
                deleted_rules_id.append(x)
                break
        logging.error("Following Synthetic conditions have deleted : " + str(deleted_rules_id))
        email_alert = True
    elif reference_synthetic_rule_count < current_synthetic_rule_count:
        reset_reference_rules.reset_synthetic_configurations()

    if email_alert:
        send_email_alert(email_alert)


with open('config.json') as config_file:
    configuration = json.load(config_file)

    if configuration['reset_rules_infrastructure']:
        reset_reference_rules.reset_infrastructure_configurations()
    if configuration['reset_rules_synthetic']:
        reset_reference_rules.reset_synthetic_configurations()
    if configuration['rule_verification']:
        verify()
