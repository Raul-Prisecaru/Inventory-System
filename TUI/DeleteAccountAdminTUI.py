import random
import sqlite3

from Features.AccountStatus import AccountStatus
from Features.AddNewInventory import *
from Features.DeleteAccount import deleleAccount
from Features.DisplayLogs import addToLogs
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


def displayDeleteAdmin():
    retryCounter = 0
    while retryCounter < 3:
        print('Authentication Required: ')
        password = input('Enter Your Password: ')
        if Login(session.logUser, password):
            addToLogs(f'{session.logUser} has successfully authenticated')
            confirmRandom = random.randint(1000, 9999)
            connection = sqlite3.connect(database_path)
            cursor = connection.cursor()
            while retryCounter < 3:
                AccountList = []
                cursor.execute(f'SELECT CustomerID, Username, Permission FROM LoginInformation WHERE Permission != "Admin"')
                CustomerUsername = cursor.fetchall()

                for row in CustomerUsername:
                    AccountList.append(row[0])
                    print(f''' User Accounts
                    CustomerID: {row[0]}
                    Username: {row[1]}
                    Permission: {row[2]}
                    ---------Next User---------
                    ''')

                print(f'''
                Delete Account Created on the System
                Select the Account ID you want to deal with
                ''')

                AccountID = int(input(f''' :: '''))
                while True:
                    confirmDelete = int(input(f'''Are you absolutely 100% you wish to DELETE the following account?
                    Every Data that is associated with the account will be DELETED and NOT RECOVERABLE
                    To Confirm you want to proceed with the process, enter the following code:
                    Code: {confirmRandom}
                        :: '''))

                    if confirmDelete == confirmRandom:
                        deleleAccount(AccountID, True)
                        print(f'{AccountID} has been deleted from the system')
                        addToLogs(f'{session.logUser} has successfully deleted CustomerID: {AccountID} from System')
                        break
                    else:
                        print('Invalid Code')
                        addToLogs(f'{session.logUser} has failed to enter correct code to delete account')
                break
            break

        else:
            retryCounter += 1
            print('Incorrect Password')
            addToLogs(f'{session.logUser} has failed to authenticate: {retryCounter}')
        if retryCounter == 3:
            connection = sqlite3.connect(database_path)
            cursor = connection.cursor()
            username = session.logUser
            sql_query = "UPDATE LoginInformation SET AccountStatus = 'Locked' WHERE Username = ? AND Username NOT LIKE 'Admin' "
            cursor.execute(sql_query, (username,))
            addToLogs(f'{session.logUser} has been locked due to failure to authenticate')
            connection.commit()
            connection.close()

            print('''[❌ ATTENTION NEEDED!] Account Locked for Security Purposes
                Contact Admin to Unlock Account''')
            quit()


def run():
    while True:
        displayDeleteAdmin()
        con = int(input('''Do you want to delete another record?
        [1] - Yes
        [2] - No'''))

        if con == 1:
            continue
        else:
            quit()
