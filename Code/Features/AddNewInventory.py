import sqlite3

def addNewInventory(column):
    connection = sqlite3.connect("Code/Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    select_query = f"INSERT INTO {column} VALUES (?, ?, ?);"
    cursor.execute(select_query)

if __name__ == '__main__':
    pass