from app import app, db
from modelos import *
import pymysql

def create_database(db_name, host="localhost", user="bruno", passwd="1234"):
    try:
        connection = pymysql.connect(host=host, user=user, passwd=passwd)
        cursor = connection.cursor()
        sql = f"DROP DATABASE IF EXISTS {db_name}"
        cursor.execute(sql)
        sql = f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        cursor.execute(sql)
        connection.close()
    except pymysql.Error as e:
        return str(e)

with app.app_context():
    create_database("db_quie_isso")
    db.create_all()