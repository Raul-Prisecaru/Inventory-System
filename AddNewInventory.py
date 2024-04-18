import sqlite3


def getAllColumns(Table):
    # List
    columnList = []

    # Connect To Database
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()
    selectQuery = cursor.execute(f"SELECT * FROM {Table}")

    # Get all information from Table and store to list
    for row in selectQuery.description:
        columnList.append(row[0])

    # return list with columns
    return columnList


def getPlaceholders(Table):
    # List
    placeholderValues = []

    # Connect To Database
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    # Get number of columns from Table
    Values = len(getAllColumns(Table))
    print(f"Function getPlaceHolders Values: {Values}")

    # # Used to format all the Placeholders in a list to be later used in the SQL query
    for _ in range(Values):
        placeholderValues.append(", ".join("?"))

    print(f"Function getPlaceHolders Placeholders ?: {placeholderValues}")
    # Return list with placeholders
    return placeholderValues


def addToInventory(Table, values):
    # Connect to Database
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    # Store columns and placeholders functions in appropriate variables.
    columns = getAllColumns(Table)
    placeHolders = getPlaceholders(Table)

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    select_query = f"INSERT INTO {Table} ({','.join(columns)}) VALUES ({placeHolders})"

    # Execute SQLQuery and values that user provides
    cursor.execute(select_query, values)

    # Commit and Close Connection
    connection.commit()
    connection.close()


print(getAllColumns('Inventory'))
getPlaceholders('Inventory')
