import sqlite3


def getAllColumns(Table):
    columnList = []

    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()
    selectQuery = cursor.execute(f"SELECT * FROM {Table}")

    for row in selectQuery.description:
        columnList.append(row[0])

    # pop(0) removes the first item in the list
    columnList.pop(0)
    return columnList


def getPlaceholders(Table):
    placeholderValues = []
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {Table}")
    columns = cursor.fetchall()

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

    columns = getAllColumns(Table)
    # placeholders = getPlaceholders(Table)

    # Construct the SET clause dynamically
    for column in columns:
        setClause = ', '.join(f'{column} = ?')

    # Construct the UPDATE query
    update_query = f"UPDATE {Table} SET {setClause} WHERE NOT LIKE '%ID'"

    # Execute the query
    cursor.execute(update_query, values)

    connection.commit()
    connection.close()
