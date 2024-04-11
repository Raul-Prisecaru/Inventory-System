import sqlite3

def addNewInventory(column):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({column});")
    columns = cursor.fetchall()
    # Count the columns
    numberColumns = len(columns)
    print(numberColumns)

    totalValues = ", ".join('?' for _ in range(numberColumns))
    print(totalValues)
    # placeholders = ', '.join(['?'] * len(columns))
    # select_query = f"INSERT INTO {column}({', '.join(columns)}) VALUES ({placeholders});"

    # cursor.execute(select_query)

    connection.commit()
    connection.close()

if __name__ == '__main__':
    addNewInventory("ExternalCompanies")