import sqlite3
import os

from Features.GenerateLogs import addToLogs
from Features.Login import *
import Features.session as session

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def getAllColumns(Table):
    # List
    columnList = []

    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    selectQuery = cursor.execute(f"SELECT * FROM {Table}")

    # Get all information from Table and store to list
    for row in selectQuery.description:
        columnList.append(row[0])

    # Remove the first column (ID column) with pop(0)
    columnList.pop(0)
    return columnList


def getPlaceholders(Table):

    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Get all results from table and use fetchall to store each row as a tuple
    cursor.execute(f"SELECT * FROM {Table}")
    columns = cursor.fetchall()

    # Get number of columns from Table then subtract -1 to not include ID
    Values = len(columns[0])

    # Used to format all the Placeholders in a list to be later used in the SQL query
    placeholderValues = ", ".join(["?" for _ in range(Values - 1)])

    # Return list with placeholders
    return placeholderValues

def addToSystem(Table, values):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Store columns and placeholders functions in appropriate variables.
    columns = getAllColumns(Table)
    placeholders = getPlaceholders(Table)

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    cursor.execute(f"INSERT INTO {Table} ({','.join(columns)}) VALUES ({placeholders})", (values))

    # Commit and Close Connection
    connection.commit()
    connection.close()

    addToLogs(session.logUser, f'{session.logUser} has added {values} to {Table}')

def GenerateAlert(LowStockLevel=10):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute(f'SELECT InventoryID, InventoryName, StockLevel FROM Inventory WHERE StockLevel <= {LowStockLevel}')
    rows = cursor.fetchall()

    if not rows:
            print('[✔️] No Items is Currently Running Low On Stock!')
    else:
        for row in rows:
            print(f'''[❌ ATTENTION NEEDED!] The Following Stocks are Running Low
            ID | Name | Stock
            ------------------------------------
            {row[0]} | {row[1]} | {row[2]}''')


def displayCustomerInventory():
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    cursor.execute("SELECT InventoryID, InventoryName, StockLevel FROM Inventory")
    rows = cursor.fetchall()

    for row in rows:
        print(row)