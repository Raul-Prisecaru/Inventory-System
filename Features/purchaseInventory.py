import sqlite3
import os

# from Features.AddNewInventory import addToSystem

# from Features.Login import *


# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

def getCustomerID(Username):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    # Come back to this
    cursor.execute(f'SELECT CustomerID FROM viewCustomerLogin WHERE ')

def CustomerPurchase(ID, Stock):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    cursor.execute(f"""UPDATE Inventory SET StockLevel = StockLevel - {Stock} WHERE InventoryID = {ID}""")

    # Commit and Close Connection
    connection.commit()
    connection.close()


def confirmationPurchase(ID, Stock, Username):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Prepare the query with placeholders for variables
    cursor.execute(f'''
        SELECT 
            InventoryID,
            InventoryName,
            InventoryPrice * {Stock} AS FormattedPrice,
            StockLevel
        FROM 
            Inventory 
        WHERE 
            InventoryID = {ID}
    ''')

    # Fetch the result
    confirmation = cursor.fetchone()

    if confirmation:
        inventory_id, inventory_name, total_price, stock_level_check = confirmation
        stock_level = stock_level_check
        if stock_level < 0:
            print("Error: No stock available \n")
            return False

        userConfirmation = int(input(f'''Do you want to proceed?
        Inventory ID: {inventory_id} 
        Inventory Name: {inventory_name}
        Total Price: {total_price}                          

        [1] - Proceed
        [2] - Cancel
        :: '''))

        if userConfirmation == 1:
            cursor.execute("INSERT INTO Purchase (PurchaseName, PurchaseStock, CustomerID) VALUES (?,?,?)", (inventory_name, Stock, Username))
            connection.commit()
            connection.close()
            return True
        else:
            connection.close()
            return False