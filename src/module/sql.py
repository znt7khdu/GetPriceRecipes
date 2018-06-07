import MySQLdb
import json


def sql_init():
    with open('src/config/sql.json', 'r') as f:
        json_data = json.load(f)

        con = MySQLdb.connect(
            user=json_data['user'],
            passwd=json_data['passwd'],
            host=json_data['host'],
            db=json_data['db'],
            charset='utf8'
        )

        cur = con.cursor()

        return (con, cur)
