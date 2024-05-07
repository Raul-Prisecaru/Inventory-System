import sqlite3
from Features.AddNewInventory import *
from Features.Login import *
import os
import Features.session
from Features.ModifyInventory import getAllColumnsNoID
from Features.OrderStocks import orderStocks

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def displayOrder(lowStock=300):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    cursor.execute("SELECT InventoryID, InventoryName, StockLevel FROM Inventory WHERE StockLevel <= ?", (lowStock, ))
    inventory = cursor.fetchall()

    print(f'''\nOrdering Stocks Guide:
        To Ensure that data is properly deleted from Database,
        Ensure the following:
        [1] - follow the following format
        -----------------
        [ID]
        -----------------
        [2] - Select the ID of the Inventory you wish to order more stocks for
        -----------------    
        [3] - Select from the List Below

    ''')

    for row in inventory:
        print(f''' User Accounts
        InventoryID: {row[0]}
        Inventory Name: {row[1]}
        Stock Level: {row[2]}
        ---------Next Item---------
        ''')
    InventoryID = int(input(f'''Enter the ID to order more Stocks
        :: '''))
    StockOrder = int(input(f'''How many stocks to order?
        :: '''))
    orderStocks(InventoryID, StockOrder)


def run():
    while True:
        # lowStockNumber = int(input('''Input a number to display all records that have below that stock amount
        #     :: '''))
        displayOrder()
        con = int(input('''Do you want to continue?
        [1] - Yes
        [2] - No'''))

        if con == 1:
            print('')
        else:
            break


run()