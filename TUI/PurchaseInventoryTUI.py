import sqlite3
from Features.AddNewInventory import *
from Features.purchaseInventory import CustomerPurchase, confirmationPurchase
from Features.Login import *
import os
import Features.session
from Features.ModifyInventory import getAllColumnsNoID

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


# Function to get all of the tables found in the DB
# def getAllTables():
#     # List to store all of the tables
#     tableinfo = []
#
#     # Connect to Database
#     connection = sqlite3.connect(database_path)
#     cursor = connection.cursor()
#
#     # Execute Query where the type is table and get all of the results with fetchall()
#     cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
#     tables = cursor.fetchall()
#
#     # Store the results in the table
#     for table in tables:
#         tableinfo.append(table[1])
#     # Remove the irrelevant tables
#     tableinfo.remove("sqlite_sequence")
#     tableinfo.remove("LoginInformation")
#     tableinfo.remove("logs")

# # Return List to display the tables to the user later on
# return tableinfo


def run():
    print(Features.session.logUser)
    userAnswer = []
    while True:
        print(f'''Available for purchase:
            {displayCustomerInventory()}''')

        userInput = str(input(f"""\nPurchasing Guide:
                Ensure the following:
                [1] - follow the following format
                -----------------
                [InventoryID, Quantity] 
                -----------------
                [2] - After each column, ensure you have a space between the comma such as:
                13, 123
    
                [3] - Do not enter quotations marks when entering string
                -----You May Enter-----------
                """))

        inputSplit = userInput.split(',')
        for answers in inputSplit:
            userAnswer.append(answers)

        if confirmationPurchase(userAnswer[0], userAnswer[1], session.logUser):
            print('Purchase Successful')
            CustomerPurchase(userAnswer[0], userAnswer[1])
            # addToSystem('Purchase', userAnswer)
            break
        else:
            print('Confirmation Cleared')
