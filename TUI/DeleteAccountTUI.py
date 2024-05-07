import sqlite3

from Features.AccountStatus import AccountStatus
from Features.AddNewInventory import *
from Features.DeleteAccount import deleleAccount
from Features.Login import *
import os
import Features.session
from Features.ModifyInventory import getAllColumnsNoID
from Features.UpdateAccount import updateAccount
from Features.displayProfile import displayUsername

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def displayDeleteAcc():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(f'SELECT CustomerID, Username, Permission FROM LoginInformation WHERE Permission != "Admin"')
    CustomerUsername = cursor.fetchall()

    print(f'''
    Delete Account Created on the System
    Select the Account ID you want to deal with
    ''')

    for row in CustomerUsername:
        print(f''' User Accounts
        CustomerID: {row[0]}
        Username: {row[1]}
        Permission: {row[2]}
        ---------Next User---------
        ''')
    AccountID = int(input(f''' :: '''))
    deleleAccount(AccountID)
    print(f'{AccountID} has been deleted from the system')
    connection.close()
