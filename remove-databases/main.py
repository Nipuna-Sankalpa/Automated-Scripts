import os
import yaml


def get_legitimate_db_list(webroot):
    db_array = []
    isExist = os.path.exists(webroot)
    if not isExist:
        return "Web root does not exist"
    for dirname, dirnames, filenames in os.walk(webroot):
        for directory in dirnames:
            db_yml_path = webroot + '/' + directory + "/symfony/config/database.yml"
            isExist = os.path.exists(db_yml_path)
            if isExist:
                with open(db_yml_path, "r") as configuration:
                    db_settings = yaml.load(configuration, Loader=yaml.FullLoader)
                    try:
                        tmp = db_settings['all']['doctrine']['param']['dsn']
                        literals = tmp.split(";")
                        db_name = literals[2].split("=")[1]
                        print(db_name)
                        db_array.append(db_name)
                    except yaml.YAMLError as error:
                        print(error)

    return db_array


def get_total_db_list(db_host, root_password):
    return True


def get_isolated_databases(legitimate_list, total_list):
    return True


def database_filter(db_name, db_host, root_password):
    return True


def main():
    database_array = get_legitimate_db_list("/var/lib/docker/workspace/infinity/html/OHRMStandalone")
    print(database_array)
    return True


main()
