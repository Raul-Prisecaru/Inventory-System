import sqlite3
import os

from Features.purchaseInventory import getCustomerID

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
databasePath = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


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


