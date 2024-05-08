import sqlite3
from Features.AddNewInventory import *
from Features.Login import *
import os
import Features.session

from Features.ModifyInventory import modifyAllInventory, getAllColumnsNoID

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


# Function to get all of the tables found in the DB
def getAllTables():
    # List to store all of the tables
    tableinfo = []

    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Execute Query where the type is table and get all of the results with fetchall()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Store the results in the table
    for table in tables:
        tableinfo.append(table[1])
    # Remove the irrelevant tables
    tableinfo.remove("sqlite_sequence")
    tableinfo.remove("LoginInformation")
    tableinfo.remove("logs")

    # Return List to display the tables to the user later on
    return tableinfo


def run():
    retryCounter = 0
    while retryCounter < 3:
        print('Authentication Required: ')
        password = str(input('Enter Your Password: '))
        if Login(Features.session.logUser, password):
            addToLogs('Has Successfully Validated to Modify Inventory', 'AccountValidation')
            userTable = str(input(f'''What Table do you want to Modify to? 
            All Tables Available
            -------------------
            {getAllTables()}
            -------------------
                :: '''))

            userAnswer = []
            entryID = str(input(f'''Enter ID to the entry you want to modify?
                :: '''))

            userInput = str(input(f"""\nModifying Inventory Guide:
            To Ensure that data is properly Modified,
            Ensure the following:
            [1] - follow the following format
            -----------------
            {getAllColumnsNoID(userTable)}
            -----------------
            [2] - After each column, ensure you have a space between the comma such as:
            123, Name1, Name2, 123
        
            [3] - Do not enter quotations marks when entering string
            -----You May Enter-----------
            """))

            inputSplit = userInput.split(',')
            for answers in inputSplit:
                userAnswer.append(answers)
            print(f'userAnswer: {userAnswer}')
            modifyAllInventory(userTable, userAnswer, entryID)


        else:
            retryCounter += 1
            addToLogs('Has Failed to Validated', 'Account')
            print('Incorrect Password')

        if retryCounter == 3:
            print('''[❌ ATTENTION NEEDED!] Account Locked for Security Purposes
                Contact Admin to Unlock Account''')
            addToLogs('Has Locked Their Accounts by Validation Account Password', 'AccountLock')