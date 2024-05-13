import random

from Features.AccountStatus import AccountStatus
from Features.AddNewInventory import getAllColumns
from Features.DisplayLogs import displayLogs, addToLogs
from Features.GenerateAlerts import GenerateAlert
from Features.UpdateAccount import updateAccount
from TUI.AddInventoryTUI import run as AddInventoryRun
from TUI.AccountStatusTUI import run as AccountStatusRun
from TUI.DeleteAccountAdminTUI import run as displayDeleteAdminRun
from TUI.DeleteAccountCustomerTUI import run as displayDeleteCustomerRun
from TUI.DeleteRecordsTUI import run as deleteRecordsRun
from TUI.PurchaseInventoryTUI import run as PurchaseInventoryRun
from TUI.ModifyInventoryTUI import run as ModifyInventoryRun
from Features.Login import *
from Features.TrackShipment import getAllShipments
from Features.GenerateDatabase import run as GenerateDatabase
import Features.session as session
from Features.Permission import PermissionCheck
from TUI.OrderStocksTUI import run as OrderRun
import os

from Features.displayProfile import displayProfile, displayUsername, getAllTables, displayTable
from TUI.StaffSignUpTUI import run as StaffSignUpRun

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')
sql_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.sql')


def setup_database():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db', cached_statements=70)
        cursor = connection.cursor()

        with open('Database/CentralisedDatabase.sql', "r") as sql_file:
            sql_script = sql_file.read()
        cursor.executescript(sql_script)

        cursor.execute(
            "INSERT INTO LoginInformation (Username, Password, Permission, CustomerID) VALUES ('Admin', 'Admin', 'Admin', 1);")
        cursor.execute(
            "INSERT INTO LoginInformation (Username, Password, Permission, CustomerID) VALUES ('Staff', 'Staff', 'Staff', 2);")
        cursor.execute(
            "INSERT INTO LoginInformation (Username, Password, Permission, CustomerID) VALUES ('Customer', 'Customer', 'Customer', 3)")
        connection.commit()

        print('DATABASE successfully created')
    except Exception as e:
        print("Error Caught: " + str(e))


def displayOptions():
    if PermissionCheck(session.logUser) == 'Admin':
        userInput = int(input("""Welcome to St Mary's Inventory Table
            What would you like to do?
                [1] - Manage All Table
                [2] - Track All Shipments
                [3] - View Records from Table
                [4] - View Logs
                [5] - Admin Tools
                [6] - View Account Information
                [7] - Quit
                    :: """))
    elif PermissionCheck(session.logUser) == 'Staff':
        userInput = int(input("""Welcome to St Mary's Inventory Table
            What would you like to do?
                [1] - Add/Check Table
                [2] - Track All Shipments
                [3] - View Inventory
                [4] - View Account Information
                [5] - Quit
                    :: """))
    elif PermissionCheck(session.logUser) == 'Customer':
        userInput = int(input("""Welcome to St Mary's Inventory Table
            What would you like to do?
                [1] - Purchase Items
                [2] - View Your information
                [3] - Delete Your Account
                [4] - Quit
                    :: """))

    else:
        print('Your Account has an Invalid Permission.')

    return userInput


if __name__ == '__main__':
    while True:
        userLoginSignup = int(input('''Do you want to:
        [1] - Login
        [2] - Signup
        [3] - Exit
        [1234] - Emergency Database Reset
            :: '''))
        if userLoginSignup == 1:
            username = str(input('Enter Your Username: '))
            password = str(input('Enter Your Password: '))
            if Login(username, password):
                session.logUser = username
                addToLogs(f'{username} has logged onto the system')
                while True:
                    if PermissionCheck(session.logUser) == 'Admin':
                        match displayOptions():
                            case 1:
                                print('You have selected: Add/Check Table')
                                InventoryOption = int(input('''What would you like to do?
                                [1] - Add to Database
                                [2] - Check for Low Stocks
                                [3] - Delete record of Database
                                [4] - Order New Inventory
                                [5] - Modify Inventory
                                 
                                 :: '''))

                                match InventoryOption:
                                    case 1:
                                        print('You have selected: Add to Database')
                                        AddInventoryRun()

                                    case 2:
                                        print('You have selected: Check for Low Stocks')
                                        GenerateAlert()

                                    case 3:
                                        print('You have selected: Delete Record of Database')
                                        deleteRecordsRun()

                                    case 4:
                                        print('You have selected: Order New Inventory')
                                        OrderRun()

                                    case 5:
                                        print('You have selected: Modify Tables')
                                        ModifyInventoryRun()

                                    case _:
                                        print('Invalid Option')

                            case 2:
                                try:
                                    print('You have selected: Track Shipment')
                                    Inout = int(input('''Do you want to see Incoming or Outgoing Schedules?
                                                            [1] - Incoming
                                                            [2] - Outgoing
                                                            [3] - Back
                                                                ::'''))
                                    if Inout != 3:
                                        getAllShipments(Inout)
                                    elif Inout == 3:
                                        continue
                                    else:
                                        print('Invalid Option')
                                except ValueError as VE:
                                    print(f'Only Values Allowed: {str(VE)}')
                            case 3:
                                print('You have Selected: View Records from Table')
                                AdminTable = str(input(f'''
                                Select Which Table To Display:
                                {getAllTables()}
                                 :: '''))
                                if AdminTable in getAllTables():
                                    displayTable(AdminTable)
                                    addToLogs(f'{session.logUser} has viewed all records from {AdminTable}')

                                else:
                                    print('Invalid Option, Check your Captials, Its Case-Sensitive')

                            case 4:
                                print('You have selected: View Logs')
                                displayLogs()

                            case 5:
                                AdminOption = int(input('''What would you like to do?
                                [1] - Delete Database*
                                [2] - Generate Database**
                                [3] - Lock/Unlock Account
                                [4] - Sign Up Staff
                                [5] - Delete Accounts
                                [6] - Back
                                
                                * Please Note that this will delete EVERYTHING. Proceed with caution
                                ** Please Note that this will ADD ON TOP of already EXISTING RECORDS. Proceed with caution.
                                        :: '''))

                                match AdminOption:
                                    case 1:
                                        print('Resetting Database in progress...')
                                        setup_database()
                                        addToLogs(f'{username} has deleted the database')

                                    case 2:
                                        quantity = int(input('''How many records to generate?
                                         :: '''))
                                        GenerateDatabase(quantity)
                                        addToLogs(f'{username} has added {quantity} of new records to database')
                                    case 3:
                                        print('You have selected: Lock or Unlock Account')
                                        AccountStatusRun()

                                    case 4:
                                        print('You have selected: Staff Sign Up')
                                        StaffSignUpRun()

                                    case 5:
                                        print('You have selected: Delete Accounts')
                                        displayDeleteAdminRun()

                                    case 6:
                                        continue

                                    case _:
                                        print('Invalid Option')

                            case 6:
                                print('You have selected: Display Account')
                                displayProfile(session.logUser)
                                addToLogs(f'{session.logUser} has viewed their profile')

                            case 7:
                                quit()

                            case _:
                                print('Invalid Option')
                    if PermissionCheck(session.logUser) == 'Staff':
                        match displayOptions():
                            case 1:
                                print('You have selected: Add/Check Table')
                                InventoryOption = int(input('''What would you like to do?
                                [1] - Add to Inventory
                                [2] - Check for Low Stocks
                                [3] - Delete Record off Table
                                [4] - Order New Inventory Item
                                [5] - Back
    
                                 :: '''))

                                match InventoryOption:
                                    case 1:
                                        print('You have selected: Add to Inventory')
                                        AddInventoryRun()

                                    case 2:
                                        print('You have selected: Check for Low Stocks')
                                        GenerateAlert()

                                    case 3:
                                        print('You have selected: Delete Record off Table')
                                        deleteRecordsRun()

                                    case 4:
                                        print('You have selected: Order New Inventory Item')
                                        OrderRun()

                                    case 5:
                                        continue

                                    case _:
                                        print('Invalid Option')

                            case 2:
                                try:
                                    print('You have selected: Track Shipment')
                                    Inout = int(input('''Do you want to see Incoming or Outgoing Schedules?
                                                            [1] - Incoming
                                                            [2] - Outgoing
                                                            [3] - Back
                                                                ::  '''))
                                    if Inout != 3:
                                        getAllShipments(Inout)
                                    elif Inout == 3:
                                        continue
                                    else:
                                        print('Invalid Option')
                                except ValueError as VE:
                                    print(f'Only Values Allowed: {str(VE)}')

                            case 3:
                                print('You have selected: View Inventory')
                                displayTable('viewInventory')
                                addToLogs(f'{session.logUser} has viewed Inventory')

                            case 4:
                                print('You have selected: Display Account')
                                displayProfile(session.logUser)
                                addToLogs(f'{session.logUser} has viewed their profile')

                            case 5:
                                quit()

                            case _:
                                print('Invalid Option')

                    if PermissionCheck(session.logUser) == 'Customer':
                        match displayOptions():
                            case 1:
                                print('You have selected: Purchase Inventory')
                                PurchaseInventoryRun()

                            case 2:
                                print('You have selected: Display Account')
                                displayProfile(session.logUser)
                                addToLogs(f'{session.logUser} has viewed their profile')

                            case 3:
                                print('You have selected: Delete your account')
                                displayDeleteCustomerRun()

                            case 4:
                                quit()

                            case _:
                                print('Invalid Option')

        elif userLoginSignup == 2:
            username = str(input('Enter Your Username: '))
            password = str(input('Enter Your Password: '))
            CustomerName = str(input('Enter Your Name: '))
            while True:
                CustomerEmail = str(input('Enter Your Email: '))
                if '@' in CustomerEmail:
                    break
                else:
                    print('Invalid Email, cannot find @')

            CustomerAddress = str(input('Enter Your Address: '))
            while True:
                CustomerPhoneNumber = input('Enter Your Phone Number: ')
                if len(CustomerPhoneNumber) == 11:
                    break
                else:
                    print('Phone Number must be 11 digits')

            while True:
                CustomerCreditCard = input('Enter Your Long Credit Card: ')
                if len(CustomerCreditCard) == 16:
                    break
                else:
                    print('Credit Card Number must be 16 digits')
            SignUp(username, password, CustomerName, CustomerEmail, CustomerAddress, CustomerPhoneNumber,
                   CustomerCreditCard)
            addToLogs(f'{username} has successfully signed up ')
            print('Signed Up Successfully')
            break
        elif userLoginSignup == 3:
            print('Exiting...')
            quit()

        elif userLoginSignup == 1234:
            confirmRandom = random.randint(1000, 9999)
            confirmDelete = int(input(f'''Are you absolutely 100% you wish to RESET the ENTIRE Database?
                                Every Data that is located in the Database will be DELETED and NOT RECOVERABLE
                                To Confirm you want to proceed with the process, enter the following code:
                                Code: {confirmRandom}
                                    :: '''))
            if confirmDelete == confirmRandom:
                setup_database()
                GenerateDatabase(100)
                print('Emergency Reset Database completed')
                addToLogs(f'Emergency Reset Database used.')
            else:
                print('Request Cancelled')
        else:
            print('Invalid Option')
