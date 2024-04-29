import sqlite3
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def getAllShipments():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    # cursor.execute('SELECT * FROM ')


