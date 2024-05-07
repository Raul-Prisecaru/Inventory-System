import sqlite3
import os

import Features.session as session

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def getLoginID():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    # Come back to this
    cursor.execute(f'SELECT LoginID FROM LoginInformation WHERE Username = ?', (session.logUser,))
    CustomerID = cursor.fetchone()

    # return CustomerID[0]


def addToLogs(Description, Type):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    # cursor.execute(f'''INSERT INTO logs (Username, Description, Type, LoginID)
    #             VALUES (?,?,?,?)''', (session.logUser, Description, Type, getLoginID()))

    # Commit and Close Connection
    connection.commit()
    connection.close()


def displayLogs():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM 'logs'; ")
    rows = cursor.fetchall()

    for row in rows:
        print(f'''
        LogID: {row[0]}
        Username: {row[1]}
        Description: {row[2]}
        Type: {row[3]}
        LoginID: {row[4]}
        ------Next Log------''')
