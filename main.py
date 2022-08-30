from tkinter import E
import mysql.connector

# Connector to db.

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="g00gleplUs"
)

menu_options = {
    1: "Show Databases.", 
    2: "Exit", 
    3: "Initialize Databases."
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def ShwDB():
    print('Handle option \'Option 1\'')
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)

def InitDB():
    print('Initialzation scripts for databases.')
    mycursor = mydb.cursor()
    mycursor = execute("USE mydatabase")
    mycursor = execute("CREATE TABLE Maintance (location VARCHAR(255), created ")



def option2():
    print('Handle option \'Option 2\'')
    print("")

if __name__=="__main__":
    while(True):
        print_menu()
        option=""
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                ShwDB()
            elif option == 2:
                option2()
                break
            elif option == 3:
                InitDB()
            else:
                print("Invalid option. Please enter a number between 1 and 2.\n")            
        except:
            print("Wrong input. Please enter a number ...\n")




        



# mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

# # mycursor.execute("CREATE DATABASE mydatabase")
