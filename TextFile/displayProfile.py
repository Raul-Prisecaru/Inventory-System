import sqlite3
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
databasePath = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def displayProfile():
    connection = sqlite3.connect(databasePath)
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM viewCustomer WHERE Username = ?;', ('Customer',))
    rows = cursor.fetchall()
    for row in rows:
        print(f'''User Profile:
        ---User Account---
        LoginID: {row[0]}
        Username: {row[1]}
        Password: {row[2]}
        AccountPlan: {row[3]}
        AccountStatus: {row[4]}
        ---Customer Details---
        CustomerID: {row[5]}
        Customer Name: {row[6]}
        Customer Email: {row[7]}
        Customer PhoneNumber: {row[8]}
        Customer CreditCard: {row[9]}
        RegisterDate: {row[10]}''')


displayProfile()
