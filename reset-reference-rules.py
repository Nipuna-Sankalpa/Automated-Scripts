import requests, json

records_per_page = 50
headers = {
    'Api-Key': 'NRAK-OVV5B990OXXFCGJOKC8XWDN1WZX'
}


def prepare_condition_array():
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


def reset_infrastructure_configurations():
    final_condition_array = {}
    condition_array = prepare_condition_array()
    for element in condition_array:
        final_condition_array[element['id']] = element

    with open("infrastructure-rules.json", 'w') as configuration_file:
        json.dump(final_condition_array, configuration_file)


def reset_synthetic_configurations():
    api_endpoint = "https://synthetics.newrelic.com/synthetics/api/v3/monitors"
    final_condition_array = {}
    response = requests.get(api_endpoint, headers=headers)
    condition_array = response.json()['monitors']
    for element in condition_array:
        final_condition_array[element['id']] = element

    with open("synthetic-rules.json", 'w') as configuration_file:
        json.dump(final_condition_array, configuration_file)


# reset_synthetic_configurations()
