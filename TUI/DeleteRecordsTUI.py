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
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    cursor.execute("SELECT InventoryID, InventoryName, StockLevel FROM Inventory")
    inventory = cursor.fetchall()

    print(f'''\nDeleting Records Guide:
        To Ensure that data is properly deleted from Database,
        Ensure the following:
        [1] - follow the following format
        -----------------
        [ID]
        -----------------
        [2] - Select the ID of the Inventory you wish to delete from the System
        -----------------    
        [3] - Select from the List Below
        
    ''')

    for row in inventory:
        print(f''' User Accounts
        LoginID: {row[0]}
        Username: {row[1]}
        Permission: {row[2]}
        ---------Next Item---------
        ''')
    InventoryID = int(input(f'''Enter the ID to DELETE
        :: '''))
    deleteRecords(InventoryID)


def run():
    while True:
        displayDelete()
        con = int(input('''Do you want to delete another record?
        [1] - Yes
        [2] - No'''))

        if con == 1:
            print('')
        else:
            break
