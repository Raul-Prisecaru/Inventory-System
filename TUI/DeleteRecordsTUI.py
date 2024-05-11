import sqlite3
from Features.AddNewInventory import *
from Features.Login import *
import os
import Features.session
from Features.ModifyInventory import getAllColumnsNoID

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

def displayDelete():
        # Connect to Database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        InventoryList = []

        # Select all Records from Inventory and only display the ID, Name, Stock Level
        cursor.execute("SELECT InventoryID FROM Inventory")
        inventoryID = cursor.fetchall()

        for row in inventoryID:
            print(row)
            InventoryList.append(row[0])

        # Select all Records from Inventory and only display the ID, Name, Stock Level
        cursor.execute("SELECT InventoryID, InventoryName, StockLevel FROM Inventory")
        inventory = cursor.fetchall()

        for row in inventory:
            print(f''' Inventory Item
            InventoryID: {row[0]}
            Inventory Name: {row[1]}
            Stock Level: {row[2]}
            ---------Next Item---------
            ''')
        while True:
            UserOption = int(input(f'''
            \nDeleting Records Guide:
                To Ensure that data is properly deleted from Database,
                Ensure the following:
                [1] - follow the following format
                -----------------
                [ID]
                -----------------
                [2] - Select the ID of the Inventory you wish to delete from the System
                -----------------    
                [3] - Select from the List Below
            
            Enter the ID to DELETE
                :: '''))

            if UserOption in InventoryList:
                print('Record Successfully Deleted')
                deleteRecords(UserOption)
                break
            elif UserOption not in InventoryList:
                print('Inventory Unavailable')

# Function Responsible for running the Main Logic
def run():
    # Counter for all the incorrect Authentication
    retryCounter = 0
    while retryCounter < 3:
        print('Authentication Required: ')
        password = str(input('Enter Your Password: '))

        # True if the user input correct password
        if Login(Features.session.logUser, password):

            while True:
                displayDelete()
                con = int(input('''Do you want to delete another record?
                [1] - Yes
                [2] - No'''))

                if con == 1:
                    print('')
                else:
                    quit()

        # Add to Counter and display Incorrect Password if the user didn't out correct password
        else:
            retryCounter += 1

            print('Incorrect Password')

        # Lock the Account if the user fail the validate within 3 tries
        if retryCounter == 3:
            # Connect to Database
            connection = sqlite3.connect(database_path)
            cursor = connection.cursor()
            # Store the session (Currently Logged on) to 'username'
            username = Features.session.logUser

            # Update the AccountStatus to be locked
            sql_query = "UPDATE LoginInformation SET AccountStatus = 'Locked' WHERE Username = ? AND Username NOT LIKE 'Admin' "
            cursor.execute(sql_query, (username,))

            connection.commit()
            connection.close()

            # Display the message that the Account is locked
            print('''[❌ ATTENTION NEEDED!] Account Locked for Security Purposes
                    Contact Admin to Unlock Account''')
