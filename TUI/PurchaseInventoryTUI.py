import sqlite3
from Features.AddNewInventory import *
from Features.DisplayLogs import addToLogs
from Features.purchaseInventory import CustomerPurchase, confirmationPurchase
from Features.Login import *
import os
import Features.session
from Features.ModifyInventory import getAllColumnsNoID

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

def run():
    userAnswer = []
    while True:
        print(f'''Available for purchase:
            {displayInventory()}''')

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
        print(userAnswer)

        if confirmationPurchase(userAnswer[0], userAnswer[1]):
            print('Purchase Successful')
            addToLogs(f'{session.logUser} has successfully made a purchase. InventoryID:{userAnswer[0]}, Stock:{userAnswer[1]} ')
            CustomerPurchase(userAnswer[0], userAnswer[1])
            break
        else:
            print('Confirmation Cleared')
