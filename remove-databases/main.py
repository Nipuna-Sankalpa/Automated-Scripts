import os
import yaml
import pymysql


def get_legitimate_db_list(webroot):
    db_array = []
    isExist = os.path.exists(webroot)
    if not isExist:
        return "Web root does not exist"
    for directory_first_level in os.listdir(webroot):
        secondary_web_root = webroot + '/' + directory_first_level
        print(secondary_web_root)
        for directory in os.listdir(secondary_web_root):
            db_yml_path = webroot + '/' + directory_first_level + '/' + directory + "/symfony/config/databases.yml"
            if directory_first_level == "OPENSOURCE":
                db_yml_path = webroot + '/' + directory_first_level + '/' + directory + "/symfony/web/symfony/config/databases.yml"
            isExist = os.path.exists(db_yml_path)
            if isExist:
                with open(db_yml_path, "r") as configuration:
                    db_settings = yaml.load(configuration, yaml.SafeLoader)
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
    db_connection = pymysql.connect(db_host, "root", root_password)
    db_pointer = db_connection.cursor()
    db_pointer.execute("show databases")
    result = db_pointer.fetchall()
    db_connection.close()
    return result


def database_filter(legitimate_list, database):
    if database not in legitimate_list:
        return True
    return False


def delete_databases(db_name, db_host, root_password):
    exclusion_list = ["information_schema", "mysql", "performance_schema", "requestdesk_centraldb_11_release",
                      "uat_rd_dummy_db"]
    if db_name not in exclusion_list:
        db_connection = pymysql.connect(db_host, "root", root_password)
        db_pointer = db_connection.cursor()
        db_pointer.execute("drop database `" + db_name + "`;")
        result = db_pointer.fetchone()
        db_connection.close()
        print(db_name)
        return result
    return False


def main():
    db_host = "172.40.0.102"
    root_password = "p2835GmVeBpbPLT"
    web_root = "/var/lib/docker/workspace/infinity/html/OHRMStandalone"

    database_array = get_legitimate_db_list(web_root)
    print(database_array)
    total_db_list = get_total_db_list(db_host, root_password)
    for db in total_db_list:
        db_name = db[0]
        if database_filter(database_array, db_name):
            delete_databases(db_name, db_host, root_password)
    return True


main()
