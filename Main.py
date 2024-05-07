from Features.AccountStatus import AccountStatus
from Features.AddNewInventory import GenerateAlert, getAllColumns
from Features.TermsOfService import termsService
from Features.UpdateAccount import updateAccount
from TUI.AddInventoryTUI import run as AddInventoryRun
from TUI.AccountStatusTUI import run as AdminTUIRun
from TUI.DeleteAccountTUI import displayDeleteAcc
from TUI.DeleteRecordsTUI import run as deleteRecordsRun
from TUI.PurchaseInventoryTUI import run as PurchaseInventoryRun
from TUI.ModifyInventoryTUI import run as ModifyInventoryRun
from Features.Login import *
from Features.GenerateLogs import displayLogs
from Features.TrackShipment import getAllShipments
from Features.DeveloperMode import run as GenerateDatabase
import Features.session as session
from Features.Permission import PermissionCheck
import os

from Features.displayProfile import displayProfile, displayUsername
from TUI.StaffSignUpTUI import run as StaffSignUpRun

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')
sql_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.sql')


def setup_database():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        with open('Database/CentralisedDatabase.sql', "r") as sql_file:
            sql_script = sql_file.read()
        print(sql_script)
        cursor.executescript(sql_script)

        cursor.execute("INSERT INTO LoginInformation (Username, Password, Permission, CustomerID) VALUES ('Admin', 'Admin', 'Admin', 1);")
        cursor.execute("INSERT INTO LoginInformation (Username, Password, Permission, CustomerID) VALUES ('Staff', 'Staff', 'Staff', 2);")
        cursor.execute("INSERT INTO LoginInformation (Username, Password, Permission, CustomerID) VALUES ('Customer', 'Customer', 'Customer', 3)")
        connection.commit()


    except Exception as e:
        print("Error Caught: " + str(e))


# setup_database()
# GenerateDatabase(10)
def displayOptions():
    if PermissionCheck(session.logUser) == 'Admin':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Add/Check System
                [2] - Modify System
                [3] - Track All Shipments
                [4] - View System
                [5] - View Logs
                [6] - Admin
                    :: """))
    elif PermissionCheck(session.logUser) == 'Staff':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Add/Check System
                [2] - Modify Inventory
                [3] - Track All Shipments
                [4] - View Inventory
                    :: """))
    elif PermissionCheck(session.logUser) == 'Customer':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Purchase Items
                [2] - View Your information
                [3] - Delete Your Account
                    :: """))

    else:
        print('Your Account has an Invalid Permission.')

    return userInput


userLoginSignup = int(input('''Do you want to:
[1] - Login
[2] - Signup
[3] - Exit
[4] - Emergency Reset
    :: '''))
username = str(input('Enter Your Username: '))
password = str(input('Enter Your Password: '))

if __name__ == '__main__':
    if userLoginSignup == 1:
        if Login(username, password):
            session.logUser = username
            print(f'logUser: {session.logUser}')
            print('Login Successful')
            while True:
                if PermissionCheck(session.logUser) == 'Admin':
                    match displayOptions():
                        case 1:
                            print('You have selected: Add/Check System')
                            InventoryOption = int(input('''What would you like to do?
                            [1] - Add to Database
                            [2] - Check for Low Stocks
                            [3] - Delete record off Database
                             
                             :: '''))


                            match InventoryOption:
                                case 1:
                                    AddInventoryRun()

                                case 2:
                                    GenerateAlert()

                                case 3:
                                    deleteRecordsRun()

                        case 2:
                            print('You have selected: Modify System')
                            ModifyInventoryRun()

                        case 3:
                            print('You have selected: Track Shipment')
                            Inout = int(input('''Do you want to see Incoming or Outgoing Schedules?
                                                    [1] - Incoming
                                                    [2] - Outgoing'''))
                            getAllShipments(Inout)

                        case 4:
                            print('You have selected: Display Inventory')
                            getAllColumns('Inventory')

                        case 5:
                            print('You have selected: View Logs')
                            displayLogs()

                        case 6:
                            AdminOption = int(input('''What would you like to do?
                            [1] - Delete Database*
                            [2] - Generate Database**
                            [3] - Lock/Unlock Account
                            [4] - Sign Up Staff
                            [5] - Delete Accounts
                            
                            * Please Note that this will delete EVERYTHING. Proceed with caution
                            ** Please Note that this will ADD ON TOP of already EXISTING RECORDS. Proceed with caution.
                                    :: '''))

                            match AdminOption:
                                case 1:
                                    print('Resetting Database in progress...')
                                    setup_database()
                                    print('Database successfully reset...')
                                    addToLogs('Purged The Database', 'Database')
                                case 2:
                                    quantity = int(input('''How many records to generate?
                                     :: '''))
                                    GenerateDatabase(quantity)
                                case 3:
                                    print('You have selected: Lock or Unlock Account')
                                    AdminTUIRun()
                                #
                                case 4:
                                    print('You have selected: Staff Sign Up')
                                    StaffSignUpRun()

                                case 5:
                                    print('You have selected: Delete Accounts')
                                    displayDeleteAcc()

                        case _:
                            print('Invalid Option')
                if PermissionCheck(session.logUser) == 'Staff':
                    match displayOptions():
                        case 1:
                            print('You have selected: Add/Check System')
                            InventoryOption = int(input('''What would you like to do?
                            [1] - Add to Inventory
                            [2] - Check for Low Stocks
                            [3] - Delete Item off system

                             :: '''))

                            match InventoryOption:
                                case 1:
                                    AddInventoryRun()

                                case 2:
                                    GenerateAlert()

                                case 3:
                                    deleteRecordsRun()

                        case 2:
                            print('You have selected: Modify System')
                            ModifyInventoryRun()

                        case 3:
                            print('You have selected: Track Shipment')
                            Inout = int(input('''Do you want to see Incoming or Outgoing Schedules?
                            [1] - Incoming
                            [2] - Outgoing'''))
                            getAllShipments(Inout)

                        case 4:
                            print('You have selected: View Inventory')
                            getAllColumns('Inventory')
                        case _:
                            print('Invalid Option')

                if PermissionCheck(session.logUser) == 'Customer':
                    match displayOptions():
                        case 1:
                            print('You have selected: Purchase Inventory')
                            PurchaseInventoryRun()

                        case 2:
                            print('Option 2')
                            displayProfile(session.logUser)

                        case 3:
                            print('You have selected: Delete your account')

                        case _:
                            print('Invalid Option')

    elif userLoginSignup == 2:
        CustomerName = str(input('Enter Your Name: '))
        CustomerEmail = str(input('Enter Your Email: '))
        CustomerAddress = str(input('Enter Your Address: '))
        CustomerPhoneNumber = int(input('Enter Your Phone Number: '))
        CustomerCreditCard = int(input('Enter Your Long Credit Card: '))
        SignUp(username, password, CustomerName, CustomerEmail, CustomerAddress, CustomerPhoneNumber,
               CustomerCreditCard)
    elif userLoginSignup == 3:
        print('Exiting...')


