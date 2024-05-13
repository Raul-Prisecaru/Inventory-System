import os
import sqlite3

from Features import session
from Features.DisplayLogs import addToLogs

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def GenerateAlert(LowStockLevel=150):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Get ID, Name, and Stock Level From Inventory Where StockLevel is lower than 150 (Default Value)
    cursor.execute(f'''SELECT InventoryID, InventoryName, StockLevel 
        FROM Inventory 
        WHERE StockLevel <= {LowStockLevel}''')
    rows = cursor.fetchall()
    addToLogs(f'{session.logUser} has checked for low Stock ')
    # If nothing is found then display no items is on low stock
    if not rows:
        print('[✔️] No Items is Currently Running Low On Stock!')
    # If something is found then display the ID, Name, and Stocks of those Low Stocks Inventory
    else:
        for row in rows:
            print(f'''[❌ ATTENTION NEEDED!] The Following Stocks are Running Low
            ID: {row[0]}
            Name: {row[1]}
            Stock: {row[2]}''')
