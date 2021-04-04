import os
import logging
from dateutil.relativedelta import relativedelta
from elasticsearch import Elasticsearch
import yaml
from datetime import datetime


def getConfigurations(index):
    with open("config.yml", "r") as configuration_registry:
        configuration = yaml.load(configuration_registry, yaml.SafeLoader)
    if index in configuration['settings'].keys():
        return configuration['settings'][index]
    return False


def archiveIndexList():
    host = getConfigurations("host")
    port = getConfigurations("port")
    log_retention_period = getConfigurations("data-retention-period")
    current_date = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
    delta = relativedelta(months=log_retention_period)
    logs_delete_from = current_date - delta
    es = Elasticsearch([{'host': host, 'port': port}])
    index_list = es.cat.indices(index='logstash-*', format="JSON", h="index,creation.date.string")

    for x in index_list:
        date_string = x['creation.date.string']
        date_object = datetime.strptime(date_string.split('T')[0], "%Y-%m-%d")
        if date_object < logs_delete_from:
            result = archiveIndex(x['index'])
            es.indices.delete(index=x['index'], ignore_unavailable=True)
    return result


def deleteIndex():
    return True


def archiveIndex(index):
    host = getConfigurations("host")
    port = getConfigurations("port")
    archive_log_path = getConfigurations("archive-directory")
    binary_path = getConfigurations('elastic-dump-binary')

    dump_map = binary_path + " --fsCompress --delete --input=http://" + host + ":" + port + "/" + index + " --output=" + \
               archive_log_path + index + "map.gz --type=mapping"
    dump_data = binary_path + " --fsCompress --delete --input=http://" + host + ":" + port + "/" + index + " --output=" + \
                archive_log_path + index + "data.gz --type=data"

    try:
        result = os.system(dump_map + " && " + dump_data)
        logging.info(dump_map)
        logging.info(dump_data)
        return result
    except:
        logging.error(dump_map)
        logging.error(dump_data)

    return False


def pushRemoteCloud():
    return True


logging.basicConfig(filename=getConfigurations('error-log-path'), format='%(asctime)s - %(message)s',
                    level=logging.INFO)

archiveIndexList()
