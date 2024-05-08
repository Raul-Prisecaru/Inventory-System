import random
import sqlite3

from Features.AccountStatus import AccountStatus
from Features.AddNewInventory import *
from Features.DeleteAccount import deleleAccount
from Features.Login import *
import os
import Features.session as session
from Features.ModifyInventory import getAllColumnsNoID
from Features.UpdateAccount import updateAccount
from Features.displayProfile import displayUsername

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def getCustomerID():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    # Come back to this
    cursor.execute(f'SELECT CustomerID FROM LoginInformation WHERE Username = ?', (session.logUser,))
    CustomerID = cursor.fetchone()

    return CustomerID[0]


def displayDeleteCustomer():
    retryCounter = 0
    while retryCounter < 3:
        print('Authentication Required: ')
        password = input('Enter Your Password: ')
        confirmRandom = random.randint(1000,9999)
        if Login(session.logUser, password):
            confirmDelete = int(input(f'''Are you absolutely 100% you wish to DELETE your account?
            Every Data that is associated with this account will be DELETED and NOT RECOVERABLE
            To Confirm you want to proceed with the process, enter the following code:
            Code: {confirmRandom}
                :: '''))

            if confirmDelete == confirmRandom:
                deleleAccount(getCustomerID(), True)
                print('Account Successfully Deleted')
                quit()
            else:
                print('Invalid code')

        else:
            retryCounter += 1
            addToLogs('Has Failed to Validate', 'AccountValidation')
            print('Incorrect Password')

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    username = session.logUser
    print(username)
    sql_query = "UPDATE LoginInformation SET AccountStatus = 'Locked' WHERE Username = ?"
    cursor.execute(sql_query, (username,))

    connection.commit()
    connection.close()
    print('''[❌ ATTENTION NEEDED!] Account Locked for Security Purposes
        Contact Admin to Unlock Account''')
    addToLogs('Has Locked Their Accounts by failing to validation Account Password', 'AccountLock')
    return False
