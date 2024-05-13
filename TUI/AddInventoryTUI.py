import sqlite3
from Features.AddNewInventory import *
from Features.DisplayLogs import addToLogs
from Features.Login import *
import os
import Features.session
from Features.ModifyInventory import getAllColumnsNoID

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
    tableinfo.remove("Customer")
    tableinfo.remove("Purchase")
    tableinfo.remove("Orders")

    # Return List to display the tables to the user later on
    return tableinfo


def addInventory():
    # Counter for all the incorrect Authentication
    retryCounter = 0
    while retryCounter < 3:
        print('Authentication Required: ')
        password = str(input('Enter Your Password: '))
        # True if the user input correct password
        if Login(Features.session.logUser, password):
            addToLogs(f'{Features.session.logUser} has successfully authenticated')
            while True:
                userTable = str(input(f'''What Table do you want to add to?
                            All Tables Available
                            -------------------
                            {getAllTables()}
                            -------------------
                                :: '''))

                if userTable in getAllTables():
                    userAnswer = []
                    userInput = str(input(f"""\nInserting new Inventory Guide:
                                To Ensure that data is properly inserted into Database,
                                Ensure the following:
                                [1] - follow the following format
                                -----------------
                                {getAllColumnsNoID(userTable)}
                                -----------------
                                [2] - After each column, ensure you have a space between the comma such as:
                                123, Name1, Name2, 123

                                [3] - Do not enter quotations marks when entering string
                                -----You May Enter-----------
                                     :: """))

                    inputSplit = userInput.split(',')
                    for answers in inputSplit:
                        userAnswer.append(answers)
                    print('Successfully Added to the System')
                    addToLogs(f'{Features.session.logUser} has added {userAnswer} to {userTable} ')
                    addToSystem(userTable, userAnswer)
                    break
                else:
                    print('invalid table')
            break


# Function Responsible for running the Main Logic of Adding Inventory
def run():
    while True:
        addInventory()
        try:
            con = int(input('''Do you want to delete another record?
            [1] - Yes
            [2] - No
                :: '''))

            if con == 1:
                continue
            else:
                break
        except ValueError as VE:
            print(f'Only Values Allowed: {str(VE)}')
            break
