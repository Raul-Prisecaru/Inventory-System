import sqlite3

from Features.AccountStatus import AccountStatus
from Features.AddNewInventory import *
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


def displayUpgrade():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(f'SELECT LoginID, Username, Permission FROM LoginInformation WHERE Permission = "Customer"')
    CustomerUsername = cursor.fetchall()

    print(f'''
    Upgrading Customer Accounts to Staff Accounts
    Select the Account ID you want to deal with
    ''')

    for row in CustomerUsername:
        print(f''' User Accounts
        LoginID: {row[0]}
        Username: {row[1]}
        Permission: {row[2]}
        ---------Next User---------
        ''')
    AccountID = int(input(f''' :: '''))
    updateAccount('Permission', 'Staff', AccountID)
    print(f'{AccountID} has been Upgraded to Staff')
    connection.close()


def displayDowngrade():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(f'SELECT LoginID, Username, Permission FROM LoginInformation WHERE Permission = "Staff"')
    CustomerUsername = cursor.fetchall()

    print(f'''
    Upgrading Customer Accounts to Staff Accounts
    Select the Account ID you want to deal with
    ''')

    for row in CustomerUsername:
        print(f''' User Accounts
        LoginID: {row[0]}
        Username: {row[1]}
        Permission: {row[2]}
        ---------Next User---------
        ''')
    AccountID = int(input(f''' :: '''))
    updateAccount('Permission', 'Customer', AccountID)
    print(f'{AccountID} has been Downgraded to Customer')

    connection.close()


def run():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    print(f'''
    Signing Up Staff
    When needing to create Staff accounts, you can use this system to do so
    The Account Needs to have already been Created using the Sign Up Option at the Main Menu
    This System will Upgrade/Downgrade the account to Staff/Customer

    Select the Account ID you want to deal with''')

    AccountPermission = int(input('''Do you want to:
    [1] - Upgrade Account to Staff
    [2] - Downgrade Account to Customer
        :: '''))

    if AccountPermission == 1:
        displayUpgrade()

    elif AccountPermission == 2:
        displayDowngrade()



