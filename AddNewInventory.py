import sqlite3


def getAllColumns(Table):
    columnList = []

    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()
    selectQuery = cursor.execute(f"SELECT * FROM {Table}")

    for row in selectQuery.description:
        columnList.append(row[0])

    return columnList


def getPlaceholders(Table, Values):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {Table}")
    columns = cursor.fetchall()

def addNewInventory(Table, values):
    columnList = []
    # global row
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    #Get Information About Columns
    cursor.execute(f"PRAGMA table_info({Table});")
    columns = cursor.fetchall()

    # Count the columns in a table
    numberColumns = len(columns)
    print(numberColumns)

    selectQuery = cursor.execute(f"SELECT * FROM {Table}")
    # Add placeholders with .join with a ", " for the number of columns.
    totalValues = ", ".join('?' for _ in range(numberColumns))
    print(totalValues)

    # Get Column Name with .description and add to the list.
    for row in selectQuery.description:
        columnList.append(row[0])
        print(row[0])

    print(columnList)
    allColumnNames = ', '.join(columnList)

    # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    select_query = f"INSERT INTO {Table} ({allColumnNames}) VALUES ({totalValues})"

    cursor.execute(select_query, f"{values}")

    connection.commit()
    connection.close()


if __name__ == '__main__':
    addNewInventory("Inventory")
