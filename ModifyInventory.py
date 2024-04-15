import sqlite3


def getAllColumnsNoID(Table):
    columnList = []

    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()
    selectQuery = cursor.execute(f"SELECT * FROM {Table}")

    for row in selectQuery.description:
        columnList.append(row[0])

    # pop(0) removes the first item in the list
    columnList.pop(0)
    return columnList


def getPlaceholdersNoID(Table):
    placeholderValues = []
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {Table}")
    columns = cursor.fetchall()
    # Get number of columns from Table then subtract -1 to not include ID
    Values = len(columns[0] - 1)
    print(Values)

    for _ in range(Values):
        placeholderValues.append(", ".join("?"))
    print(placeholderValues)

    return placeholderValues


def modifyOneInventory(Table, values, row):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()


def modifyAllInventory(Table, values):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    columns = getAllColumnsNoID(Table)



    # columns = getAllColumns(Table)
    #
    # Update Clause

    updateFormat = ', '.join([f'{column} = ?' for column in columns])

    updateQuery = f'UPDATE {Table} SET {updateFormat}'


    # cursor.execute(viewQuery)  # Execute the CREATE VIEW statement
    cursor.execute(updateQuery, values)  # Execute the UPDATE query

    connection.commit()
    connection.close()
    # CREATE VIEW statement to create a temporary view with all columns from the table
    # viewQuery = f"""CREATE VIEW viewTable AS
    # SELECT {', '.join(columns)}
    # FROM {Table}"""
    #
    # # Construct the UPDATE query
    # updateQuery = f"UPDATE viewTable SET {setClause}"
