import sqlite3
import os

from Features.GenerateLogs import addToLogs
from Features.Login import *
import Features.session as session

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def purchaseInventory(ID, Stock):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    select_query = f"UPDATE Inventory SET StockLevel = StockLevel - {Stock} WHERE InventoryID = {ID}"

    # Execute SQLQuery and values that user provides
    cursor.execute(select_query)

    priceQuery = f'SELECT InventoryPrice * {Stock} FROM Inventory WHERE InventoryID = {ID}'

    cursor.execute(priceQuery)
    priceTotal = cursor.fetchone()
    print(f'£{priceTotal}')

    # Commit and Close Connection
    connection.commit()
    connection.close()


# def addToStocks(value):
#     connection = sqlite3.connect(database_path)
#     cursor = connection.cursor()
#
#     cursor.execute(f"SELECT * FROM 'Inventory' LIKE 'Stock%'")
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print(row)

# def GenerateAlert(LowStockLevel=10):
#     connection = sqlite3.connect(database_path)
#     cursor = connection.cursor()
#
#     cursor.execute(f'SELECT InventoryID, InventoryName, StockLevel FROM Inventory WHERE StockLevel <= {LowStockLevel}')
#     rows = cursor.fetchall()
#
#     if not rows:
#             print('[✔️] No Items is Currently Running Low On Stock!')
#     else:
#         for row in rows:
#             print(f'''[❌ ATTENTION NEEDED!] The Following Stocks are Running Low
#             ID | Name | Stock
#             ------------------------------------
#             {row[0]} | {row[1]} | {row[2]}''')
#
#
# def displayCustomerInventory():
#     # Connect to Database
#     connection = sqlite3.connect(database_path)
#     cursor = connection.cursor()
#
#     # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
#     cursor.execute(f"SELECT * FROM viewInventory;")
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print(row)