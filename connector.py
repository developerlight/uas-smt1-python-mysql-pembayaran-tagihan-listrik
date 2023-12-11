import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database = 'db_pln'
)

mycursor = mydb.cursor()

mycursor.execute('show tables')

for x in mycursor:
    print(x)