from peewee import MySQLDatabase
import pymysql

db=MySQLDatabase(
    'sakila',
    user = 'sbrito',
    password = 'Sb40222538585',
    host = 'localhost'
    # ,
    # **{'driver': 'pymysql'}
)