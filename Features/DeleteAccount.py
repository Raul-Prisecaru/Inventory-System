import sqlite3
import os



# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def deleleAccount(CustomerID, confirmation):
    if confirmation:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM LoginInformation WHERE CustomerID = ?", (CustomerID,))
        cursor.execute(f"DELETE FROM Customer WHERE CustomerID = ?", (CustomerID,))
        cursor.execute(f"DELETE FROM Purchase WHERE CustomerID = ?", (CustomerID,))

        connection.commit()

