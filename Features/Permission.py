import sqlite3
import os

from Features.UpdateAccount import updateAccount

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def PermissionCheck(username):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    selectQuery = f'SELECT Username, Permission FROM LoginInformation WHERE Username = ?'
    cursor.execute(selectQuery, (username, ))
    result = cursor.fetchone()

    if result:
        permission = result[1]
        return permission

    if not result:
        return print('No result found')