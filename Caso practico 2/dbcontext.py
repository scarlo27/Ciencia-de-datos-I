from peewee import MySQLDatabase
import pymysql

db=MySQLDatabase(
    'sakila',
    user = 'root',
    password = 'XXX',
    host = 'localhost'
    # ,
    # **{'driver': 'pymysql'}
)
