import sqlite3
import os
# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

def getAllColumns(Table):
    # List
    columnList = []

    # Connect To Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    selectQuery = cursor.execute(f"SELECT * FROM {Table}")

    # Get all information from Table and store to list
    for row in selectQuery.description:
        columnList.append(row[0])
    print(f'columnList: {columnList}')
    # return list with columns
    return columnList


def getPlaceholders(Table):
    # List
    # placeholderValues = []

    # Connect To Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Get number of columns from Table
    Values = len(getAllColumns(Table))
    print(Values)
    # print(f"Function getPlaceHolders Values: {Values}")

    # Used to format all the Placeholders in a list to be later used in the SQL query

    placeholder = ', '.join(['?' for _ in range(Values)])
    print(placeholder)
    return placeholder


def addToInventory(Table, values):
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







