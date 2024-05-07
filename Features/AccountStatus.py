import sqlite3
import os

import Features.session as session
from Features.GenerateLogs import addToLogs

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def AccountStatus(AccountID):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(f"SELECT AccountStatus FROM LoginInformation WHERE LoginID = ?", (AccountID,))
    accStatus = cursor.fetchone()
    if accStatus[0] == 'Unlocked':
        cursor.execute(f"UPDATE LoginInformation SET AccountStatus = 'Locked' WHERE LoginID = ?", (AccountID,))
        print(f'{AccountID} is now Locked')
        addToLogs(f'{AccountID} has been Locked', 'Account')
        connection.commit()
    elif accStatus[0] == 'Locked':
        cursor.execute(f"UPDATE LoginInformation SET AccountStatus = 'Unlocked' WHERE LoginID = ?", (AccountID,))
        print(f'{AccountID} is now Unlocked')
        addToLogs(f'{AccountID} has been Unlocked', 'Account')
        connection.commit()

