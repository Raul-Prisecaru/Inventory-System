import sqlite3
from Features.AddNewInventory import *
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
    tableinfo.remove("logs")
    tableinfo.remove("Customer")
    tableinfo.remove("Purchase")
    tableinfo.remove("Orders")

    # Return List to display the tables to the user later on
    return tableinfo


def run():
    retryCounter = 0
    while retryCounter < 3:
        print('Authentication Required: ')
        password = str(input('Enter Your Password: '))
        if Login(Features.session.logUser, password):
            # print('Login Successful')
            addToLogs('Has Successfully Validated for Adding Inventory', 'AccountValidation')
            while True:
                userTable = str(input(f'''What Table do you want to add to?
                        All Tables Available
                        -------------------
                        {getAllTables()}
                        -------------------
                            :: '''))

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
                        """))

                inputSplit = userInput.split(',')
                for answers in inputSplit:
                    userAnswer.append(answers)
                print('Successfully Added to the System')
                addToSystem(userTable, userAnswer)
                # break

                con = int(input('''Do you want to continue?
                [1] - Yes
                [2] - No'''))

                if con == 1:
                    print('')
                else:
                    break

        else:
            retryCounter += 1
            addToLogs('Has Failed to Validate', 'AccountValidation')
            print('Incorrect Password')

        if retryCounter == 3:
            print(Features.session.logUser)
            connection = sqlite3.connect(database_path)
            cursor = connection.cursor()
            username = Features.session.logUser
            print(username)
            sql_query = "UPDATE LoginInformation SET AccountStatus = 'Locked' WHERE Username = ?"
            cursor.execute(sql_query, (username, ))

            connection.commit()
            connection.close()




            print('''[❌ ATTENTION NEEDED!] Account Locked for Security Purposes
                Contact Admin to Unlock Account''')
            addToLogs('Has Locked Their Accounts by failing to validation Account Password', 'AccountLock')

