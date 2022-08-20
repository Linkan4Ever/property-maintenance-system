import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="g00gleplUs"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# mycursor.execute("CREATE DATABASE mydatabase")