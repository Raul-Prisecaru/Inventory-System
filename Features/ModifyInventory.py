import sqlite3
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

def getAllColumnsByID(Table):
    # List
    columnList = []

    # Connect To Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Get all information from Table and execute
    executeQuery = f'SELECT * FROM {Table}'
    rows = cursor.execute(executeQuery)

    # Get all available Information from a table by using .description
    for row in rows.description:
        columnList.append(row)


    # Get the Column Name (First in the list)
    columnID = columnList[0]
    print(columnID)
    return columnID[0]


def getAllColumnsNoID(Table):
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


def getPlaceholdersNoID(Table):
    # List
    placeholderValues = []

    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Get all results from table and use fetchall to store each row as a tuple
    cursor.execute(f"SELECT * FROM {Table}")
    columns = cursor.fetchall()

    # Get number of columns from Table then subtract -1 to not include ID
    Values = len(columns[0])

    # Used to format all the Placeholders in a list to be later used in the SQL query
    for _ in range(Values):
        placeholderValues.append(", ".join("?"))

    # Return list with placeholders
    return placeholderValues


def modifyAllInventory(Table, values, ID):
    # Store the ID column
    GetColumnID = getAllColumnsByID(Table)

    # Connect To Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Store all Columns Except ID
    columns = getAllColumnsNoID(Table)

    # Create Format for UPDATE Query depending on number of columns: ColumnName = ?, ColumnName = ?
    updateFormat = ', '.join([f'{column} = ?' for column in columns])

    # UPDATE {Table provided by user} SET {Format Created Above} WHERE {ColumnID} = {ID provided by user}
    updateQuery = f'UPDATE {Table} SET {updateFormat} WHERE {GetColumnID} = {ID}'

    # Execute SQLQuery and values that user provides
    cursor.execute(updateQuery, values)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# getAllColumnsByID('Inventory')