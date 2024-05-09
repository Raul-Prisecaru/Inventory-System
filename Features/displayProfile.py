import sqlite3
import os

from Features.purchaseInventory import getCustomerID

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
databasePath = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')
# Function to get all of the tables found in the DB

def getAllTables():
    # List to store all of the tables
    tableinfo = []

    # Connect to Database
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    # Execute Query where the type is table and get all of the results with fetchall()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Store the results in the table
    for table in tables:
        tableinfo.append(table[1])
    # Remove the irrelevant tables
    tableinfo.remove("sqlite_sequence")
    tableinfo.remove("LoginInformation")
    tableinfo.remove("logs")

    # Return List to display the tables to the user later on
    return tableinfo


def displayUsername():
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    cursor.execute(f'SELECT Username, AccountStatus FROM LoginInformation;')
    CustomerUsername = cursor.fetchall()

    for row in CustomerUsername:
        return print(f''' User Accounts
        Username: {row[0]}
        AccountStatus: {row[1]}
        ''')

    connection.close()  # Close the database connection



def displayProfile(username):
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM viewCustomer WHERE Username = ?;', (username,))
    CustomerDetails = cursor.fetchall()

    cursor.execute('SELECT * FROM viewPurchase WHERE CustomerID = ?', (getCustomerID(),))
    purchase = cursor.fetchall()

    for detail in CustomerDetails:
        print(f'''User Profile:
        ---User Account---
        LoginID: {detail[0]}
        Username: {detail[1]}
        Password: {detail[2]}
        AccountPlan: {detail[3]}
        AccountStatus: {detail[4]}
        ---Customer Details---
        CustomerID: {detail[5]}
        Customer Name: {detail[6]}
        Customer Email: {detail[7]}
        Customer PhoneNumber: {detail[8]}
        Customer CreditCard: {detail[9]}
        RegisterDate: {detail[10]}
        ---Purchase History---''')
        for item in purchase:
            print(f'''
            PurchaseID: {item[1]}
            Item Name: {item[2]}
            Delivery Date: {item[3]}
            Quantity Purchased: {item[4]}
            -----------Next Item---------''')


def displayTable(Table):
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM {Table}')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
