from tkinter import E
import mysql.connector

# Connector to db.

print("=== Property Maintenance System ===")

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="g00gleplUs"
)

menu_options = {
    1: "Show Databases.", 
    2: "Initialize Databases and tables.",
    3: "Create maintenance post.", 
    4: "Show maintenance posts.",
    99: "Exit" 
}

def print_menu():
    print("")
    for key in menu_options.keys():
        print(key, ': ', menu_options[key])
    print("")

def ShowDatabases(): 
    print("Showing databases.")

    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)

def InitDB():
    print('Initialzation scripts for databases.')
    mycursor = mydb.cursor()
    

    try: 
        mycursor.execute("CREATE DATABASE mydatabase")
    except:
        print("Database already exists.")
    
    mycursor.execute("USE mydatabase")
    try: 
        mycursor.execute("""CREATE TABLE maintenance (
        location varchar(255),
        startTime datetime,
        endTime datetime,
        createdTime datetime, 
        cost int, 
        description varchar(255), 
        name varchar(255), 
        id int
        )""")

    except:
        print("Table 'maintenance' already created.")
        

    mycursor.execute("SHOW TABLES")
    print("Results:")

    for x in mycursor:
        print(x)
    print("\n")

def CreateMainenance():
    print("Creating maintenance. ", end='')
    mycursor = mydb.cursor()

    try:
        mycursor.execute("INSERT INTO mydatabase.maintenance (location, createdTime, description) VALUES ('Badrum', CURRENT_TIMESTAMP, 'Golvläggning')")
        print("Maintenance post created.")
    except:
        print("Something went wrong when trying to insert maintenance post.")

def ShowMaintenance():
    print("Showing maintenance posts. ")
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * from mydatabase.maintenance")
        print("Results:")
        for x in mycursor:
            print(x)
        print("\n")
    except:
        print("Something went wrong when trying to show maintenance posts.")


def Exit():
    print("Existing.")

if __name__=="__main__":
    while(True):
        print_menu()
        option=""
        try:
            option = int(input("Enter your choice: "))
            print("")
            if option == 1:
                ShowDatabases()
            elif option == 99:
                Exit()
                break
            elif option == 2:
                InitDB()
            elif option == 3:
                CreateMainenance()
            elif option == 4:
                ShowMaintenance()
            else:
                print("Invalid option. Please enter a number between 1 and 3.\n")            
        except:
            print("Wrong input. Please enter a number ...\n")




        



# mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

# # mycursor.execute("CREATE DATABASE mydatabase")
