import mysql.connector

# mydb = mysql.connector.connect(
#     host="192.168.1.235",
#     user="testuser",
#     password="g00gleplUs!", 
#     database="prod_pms")

mydb = mysql.connector.connect(
    host="192.168.1.235",
    user="root",
    password="g00gleplUs!")

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("Show databases")
for i in mycursor:
    print(i)