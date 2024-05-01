import sqlite3
import os

from Features.AddNewInventory import getPlaceholders, getAllColumns
from Features.ModifyInventory import getAllColumnsNoID, getPlaceholdersNoID

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def addToLogs(Table, values):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Store columns and placeholders functions in appropriate variables.
    columns = getAllColumns(Table)
    placeholders = getPlaceholders(Table)

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    select_query = f"INSERT INTO {Table} ({','.join(columns)}) VALUES ({placeholders})"

    # Execute SQLQuery and values that user provides
    cursor.execute(select_query, values)

    # Commit and Close Connection
    connection.commit()
    connection.close()

# values = [124,'Admin', 'Stock added']
# addToLogs('logs', values)


