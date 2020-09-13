import os
import yaml
import pymysql

web_root = "/var/lib/docker/workspace/jade/html/OHRMStandalone"
db_host = "172.70.0.102"
db_user = "root"
root_password = "1z5mMo@TxG7R"
soft_deletion = True


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
    db_connection = pymysql.connect(db_host, db_user, root_password)
    db_pointer = db_connection.cursor()
    db_pointer.execute("show databases")
    result = db_pointer.fetchall()
    db_connection.close()
    return result


def database_filter_by_date(time_period):
    sql_query = "SELECT table_schema,MIN(create_time) create_time FROM information_schema.tables Group by " \
                "TABLE_SCHEMA having create_time < DATE(NOW()) - INTERVAL " + time_period + "DAY Order by create_time " \
                                                                                            "desc;"
    db_connection = pymysql.connect(db_host, db_user, root_password)
    db_pointer = db_connection.cursor()
    db_pointer.execute(sql_query)
    result = db_pointer.fetchall()
    db_connection.close()
    final_list = []
    if result.count() <= 0:
        return []

    result_list = list(result)
    for x in result_list:
        final_list.append(x[0])

    return final_list


def database_filter(database):
    legitimate_list = get_legitimate_db_list(web_root)
    old_databases = database_filter_by_date("7")

    if database in legitimate_list:
        return False
    if database not in old_databases:
        return False
    return True


def delete_databases(db_name, db_host, root_password):
    exclusion_list = ["information_schema", "mysql", "performance_schema"]
    if db_name not in exclusion_list:
        db_connection = pymysql.connect(db_host, db_user, root_password)
        db_pointer = db_connection.cursor()
        if soft_deletion:
            print(db_name)
        else:
            db_pointer.execute("drop database `" + db_name + "`;")
        result = db_pointer.fetchone()
        db_connection.close()

        return result
    return False


def main():
    total_db_list = get_total_db_list(db_host, root_password)
    for db in total_db_list:
        db_name = db[0]
        if database_filter(db_name):
            delete_databases(db_name, db_host, root_password)
    return True


main()
