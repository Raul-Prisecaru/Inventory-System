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
    placeholderValues = []
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {Table}")
    columns = cursor.fetchall()

    Values = len(columns[0])
    print(Values)

    for _ in range(Values):
        placeholderValues.append(", ".join("?"))

    return placeholderValues

def addToInventory(Table, values):
    # Connect to Database
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    columns = getAllColumns(Table)
    placeHolders = getPlaceholders(Table)

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    select_query = f"INSERT INTO {Table} ({','.join(columns)}) VALUES ({placeHolders})"

    # Execute
    cursor.execute(select_query, values)

    # Commit and Close Connection
    connection.commit()
    connection.close()

# Testing Functions
if __name__ == '__main__':
    pass
    # addToInventory("Inventory")