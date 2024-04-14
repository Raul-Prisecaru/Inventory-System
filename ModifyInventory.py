import sqlite3

def getAllColumns(Table):
    columnList = []

    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()
    selectQuery = cursor.execute(f"SELECT * FROM {Table}")

    for row in selectQuery.description:
        columnList.append(row[0])

    return columnList


def getPlaceholders(Table):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {Table}")
    columns = cursor.fetchall()

    Values = len(columns[0])
    print(Values)

    placeholderValues = ", ".join('?' for _ in range(Values))
    print(placeholderValues)

    return placeholderValues

def modifyInventory(Table, values, ID):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor();

    columns = getAllColumns(Table)
    Placeholders = getPlaceholders(Table)

    AlterQuery = f"""UPDATE {Table} SET {columns} = {Placeholders} WHERE '%ID' = {ID}"""

    connection.commit()
    connection.close()