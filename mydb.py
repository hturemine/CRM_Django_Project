#Install MySQL
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install my-sql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'HoangTuan_2004',
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE dcrm_db")

print("DONE!")