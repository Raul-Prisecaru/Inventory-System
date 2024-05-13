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

def purchaseInventory():
    # Counter for all the incorrect Authentication
    retryCounter = 0
    while retryCounter < 3:
        print('Authentication Required: ')
        password = str(input('Enter Your Password: '))
        # True if the user input correct password
        if Login(Features.session.logUser, password):
            userAnswer = []
            print(f'''Available for purchase:
                   {displayInventory()}''')
            while True:
                try:
                    userAnswer.clear()
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
                                :: """))

                    inputSplit = userInput.split(',')
                    for answers in inputSplit:
                        userAnswer.append(answers)
                    print(userAnswer)

                    if confirmationPurchase(userAnswer[0], userAnswer[1]):
                        print('Purchase Successful')
                        addToLogs(
                            f'{session.logUser} has successfully made a purchase. InventoryID:{userAnswer[0]}, Stock:{userAnswer[1]} ')
                        CustomerPurchase(userAnswer[0], userAnswer[1])
                        break
                except Exception as e:
                    print(f'''
                    Error due to most likely not selecting appropriate selections. 
                    Please Review your options and try again
                    Error: {str(e)}''')
            break

        # Add to Counter and display Incorrect Password if the user didn't out correct password
        else:
            retryCounter += 1
            addToLogs(f'{Features.session.logUser} has failed to authenticate: {retryCounter} ')
            print('Incorrect Password')

        # Lock the Account if the user fail the validate within 3 tries
        if retryCounter == 3:
            # Connect to Database
            connection = sqlite3.connect(database_path)
            cursor = connection.cursor()
            # Store the session (Currently Logged on) to 'username'
            username = Features.session.logUser

            # Update the AccountStatus to be locked
            sql_query = "UPDATE LoginInformation SET AccountStatus = 'Locked' WHERE Username = ? AND Username NOT LIKE 'Admin' "
            cursor.execute(sql_query, (username,))

            connection.commit()
            connection.close()
            addToLogs(
                f'{Features.session.logUser} has been locked out of the account due to failure to authenticate')

            # Display the message that the Account is locked
            print('''[❌ ATTENTION NEEDED!] Account Locked for Security Purposes
                       Contact Admin to Unlock Account''')
            quit()


def run():
    while True:
        purchaseInventory()
        try:
            con = int(input('''Do you want to do purchase another Item?
            [1] - Yes
            [2] - No'''))

            if con == 1:
                continue
            else:
                break
        except ValueError:
            break
