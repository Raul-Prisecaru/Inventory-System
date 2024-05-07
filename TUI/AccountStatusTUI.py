import sqlite3

from Features.AccountStatus import AccountStatus
from Features.AddNewInventory import *
from Features.Login import *
import os
import Features.session
from Features.ModifyInventory import getAllColumnsNoID
from Features.displayProfile import displayUsername

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


# Function to get all of the tables found in the DB
def display():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(f'SELECT LoginID, Username, AccountStatus FROM LoginInformation;')
    CustomerUsername = cursor.fetchall()

    return CustomerUsername


def run():
    displayUser = display()

    AccStatus = int(input(f'''
    Locking/Unlocking Accounts
    When needing to Lock or Unlock accounts, you can use this system to do so
    This will swap the Account Status so:
    Lock Account --> Unlocked Account
    Unlocked Account --> Lock Account
    
    Select the Account ID you want to deal with
    
    LoginID: {displayUser[0]}
    Username: {displayUser[1]}
    AccountStatus: {displayUser[2]}
     :: '''))

    AccountStatus(AccStatus)

