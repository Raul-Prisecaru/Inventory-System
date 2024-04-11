import sqlite3

def addNewInventory(column):
    global row
    columnList = []
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({column});")
    selectQuery = cursor.execute(f"SELECT * FROM {column}")
    columns = cursor.fetchall()
    # Count the columns
    numberColumns = len(columns)
    print(numberColumns)

    totalValues = ", ".join('?' for _ in range(numberColumns))
    print(totalValues)

    for row in selectQuery.description:
        columnList.append(row[0])
        print(row[0])


    print(columnList)
    select_query = f"INSERT INTO {column} ({', '.join(columnList)}) VALUES ({totalValues})"

    cursor.execute(select_query, ("1", "1", "1", "1", "1"))

    connection.commit()
    connection.close()

if __name__ == '__main__':
    addNewInventory("Inventory")