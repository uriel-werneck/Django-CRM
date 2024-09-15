import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='senha123'
)

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE elderco')

print('Database created!')