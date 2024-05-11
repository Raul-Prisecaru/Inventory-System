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


def displayOrder(lowStock=150):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    while True:
        userOption = int(input(f'''Do you want to display only low stocks (=<{lowStock}) or all Items?
        [1] - Only Low Stocks
        [2] - All Items'''))

        if userOption == 1:
            InventoryList = []

            # Select all Records from Inventory and only display the ID, Name, Stock Level
            cursor.execute("SELECT InventoryID, InventoryName, StockLevel FROM Inventory WHERE StockLevel <= ?",
                           (lowStock,))
            inventory = cursor.fetchall()

            for row in inventory:
                print(row)
                InventoryList.append(row[0])

            for row in inventory:
                print(f''' Inventory
                InventoryID: {row[0]}
                Inventory Name: {row[1]}
                Stock Level: {row[2]}
                ---------Next Item---------
                ''')

            print(f'''\nOrdering Stocks Guide:
                To Ensure that data is properly deleted from Database,
                Ensure the following:
                [1] - follow the following format
                -----------------
                [ID]
                [Stocks] (you will be asked to enter this after entering ID)
                -----------------
                [2] - Select the ID of the Inventory you wish to order more stocks for
                -----------------    
                [3] - Select from the List Below
            ''')
            while True:
                InventoryID = int(input(f'''Enter the ID to order more Stocks
                    :: '''))
                if InventoryID in InventoryList:
                    StockOrder = int(input(f'''How many stocks to order?
                        :: '''))
                    orderStocks(InventoryID, StockOrder)
                    break
                else:
                    print('Invalid ID')

        if userOption == 2:
            InventoryList = []

            # Select all Records from Inventory and only display the ID, Name, Stock Level
            cursor.execute("SELECT InventoryID, InventoryName, StockLevel FROM Inventory")
            inventory = cursor.fetchall()

            for row in inventory:
                print(row)
                InventoryList.append(row[0])

            for row in inventory:
                print(f''' Inventory
                InventoryID: {row[0]}
                Inventory Name: {row[1]}
                Stock Level: {row[2]}
                ---------Next Item---------
                ''')

            print(f'''\nOrdering Stocks Guide:
                To Ensure that data is properly deleted from Database,
                Ensure the following:
                [1] - follow the following format
                -----------------
                [ID]
                [Stocks] (you will be asked to enter this after entering ID)
                -----------------
                [2] - Select the ID of the Inventory you wish to order more stocks for
                -----------------    
                [3] - Select from the List Below
            ''')
            while True:
                InventoryID = int(input(f'''Enter the ID to order more Stocks
                    :: '''))
                if InventoryID in InventoryList:
                    StockOrder = int(input(f'''How many stocks to order?
                        :: '''))
                    orderStocks(InventoryID, StockOrder)
                    break
                else:
                    print('Invalid ID')
        else:
            print('Invalid Option, Try Again')


def run():
    while True:
        displayOrder()
        con = int(input('''Do you want to place another order?
        [1] - Yes
        [2] - No'''))

        if con == 1:
            continue
        else:
            quit()
