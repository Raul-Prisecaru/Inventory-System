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


# Function responsible for displaying Username And AccountStatus
def displayUsername():
    # Connect to Database
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    # Execute SELECT all Query to get all Username with AccountStatus (Locked and Unlocked)
    cursor.execute(f'SELECT Username, AccountStatus FROM LoginInformation;')
    CustomerUsername = cursor.fetchall()

    # Display and Format Account Information
    for row in CustomerUsername:
        return print(f''' User Accounts
        Username: {row[0]}
        AccountStatus: {row[1]}
        ''')

    connection.close()


# Function responsible for displaying Account Profile.
def displayProfile(username):
    # Connect to database
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    # Responsible for collecting Customer Details
    # Execute SELECT all Query from View table with a condition where username match
    # Store in 'CustomerDetails'
    cursor.execute(f'SELECT * FROM viewCustomer WHERE Username = ?;', (username,))
    CustomerDetails = cursor.fetchall()

    # Responsible for collecting Purchase Details
    # Execute SELECT all Query from View table with a condition where CustomerID match
    # Store in 'Purchase'
    cursor.execute('SELECT * FROM viewPurchase WHERE CustomerID = ?', (getCustomerID(),))
    purchase = cursor.fetchall()

    # Display and format the Information presented to the User
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

# Function responsible for displaying all records from a specific table
def displayTable(Table):
    # Connect to database
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    # Execute SELECT all Query and store in 'rows'
    cursor.execute(f'SELECT * FROM {Table}')
    rows = cursor.fetchall()

    # Get Column Information
    cursor.execute(f'PRAGMA table_info({Table})')

    # Display Column Information
    pragma = cursor.fetchall()
    print(pragma)
    for row in rows:
        print(row)
