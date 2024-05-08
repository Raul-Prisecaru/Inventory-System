import sqlite3
import os

import Features.session as session
# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


# def getLoginID():
#     username = session.logUser
#     connection = sqlite3.connect(database_path)
#     cursor = connection.cursor()
#     # Come back to this
#     cursor.execute(f'SELECT LoginID FROM LoginInformation WHERE Username = ?', (username,))
#     LoginID = cursor.fetchone()
#
#     print(LoginID)
#     return LoginID

def addToLogs(Description, Type):
    loggedInUser = session.getlogUser()
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(f'SELECT LoginID FROM LoginInformation WHERE Username = ?', (loggedInUser, ))
    LoginID = cursor.fetchone()[0]


    # # INSERT INTO {Table that user provides} ({All of the columns available in the table}) VALUES ({add placeholders per column})
    cursor.execute(f'''INSERT INTO logs (Username, Description, Type, LoginID)
                VALUES (?,?,?,?)''', (loggedInUser, Description, Type, LoginID))

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
