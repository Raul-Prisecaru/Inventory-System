import sqlite3


def getAllColumns(Table):
    columnList = []
    connection = sqlite3.connect('Database/CentralisedDatabase.db')
    cursor = connection.cursor()

    executeQuery = f'SELECT * FROM {Table}'
    rows = cursor.execute(executeQuery)

    for row in rows.description:
        columnList.append(row)

    columnID = columnList[0]
    return columnID[0]


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


def modifyAllInventory(Table, values, ID):
    GetColumnID = getAllColumns(Table)
    print(GetColumnID)
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    columns = getAllColumnsNoID(Table)

    updateFormat = ', '.join([f'{column} = ?' for column in columns])

    getID = f'SELECT * FROM {Table} WHERE'

    updateQuery = f'UPDATE {Table} SET {updateFormat} WHERE {GetColumnID} = {ID}'

    # cursor.execute(viewQuery)  # Execute the CREATE VIEW statement
    cursor.execute(updateQuery, values)  # Execute the UPDATE query

    connection.commit()
    connection.close()


if __name__ == '__main__':
    print(getAllColumns('Drivers'))
