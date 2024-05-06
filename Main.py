from Features.AddNewInventory import GenerateAlert
from Features.TermsOfService import termsService
from Features.UpdateAccount import updateAccount
from TUI.AddInventoryTUI import run as AddInventoryRun
from TUI.PurchaseInventoryTUI import run as PurchaseInventoryRun
from TUI.ModifyInventoryTUI import run as ModifyInventoryRun
from Features.Login import *
from Features.GenerateLogs import displayLogs
from Features.TrackShipment import getAllShipments
from Features.DeveloperMode import run as GenerateDatabase
import Features.session as session
from Features.PermissionCheck import PermissionCheck
import os

from Features.displayProfile import displayProfile

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

        cursor.executescript(sql_script)
        print("Database Successfully Created")

        connection.commit()
        connection.close()

    except Exception as e:
        print("Error Caught: " + str(e))


# setup_database()
def displayOptions():
    if PermissionCheck(session.logUser) == 'Admin':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Add To Inventory
                [2] - Temporarily Unavailable
                [3] - Modify Inventory
                [4] - Track All Shipments
                [5] - View Inventory
                [6] - View Logs
                [7] - Admin
                    :: """))
    elif PermissionCheck(session.logUser) == 'Staff':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Add To Inventory
                [2] - Modify Inventory
                [3] - Check Inventory For Low Stocks
                [4] - Track All Shipments
                [5] - View Inventory
                    :: """))
    elif PermissionCheck(session.logUser) == 'Customer':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Purchase Items
                [2] - View Your information
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
            if PermissionCheck(session.logUser) == 'Admin':
                match displayOptions():
                    case 1:
                        print('You have selected: Add Items to Inventory')
                        AddInventoryRun()
                    case 2:
                        print('You have selected: Check Inventory for Low Stocks')

                    case 3:
                        print('You have selected: Modify System')
                        ModifyInventoryRun()

                    case 4:
                        print('You have selected: Track Shipment')
                        getAllShipments()

                    case 5:
                        print('You have selected option 5')

                    case 6:
                        print('You have selected: View Logs')
                        displayLogs()

                    case 7:
                        AdminOption = int(input('''What would you like to do?
                        [1] - Delete Database*
                        [2] - Generate Database**
                        [3] - Unblock Account
                        [4] - Sign Up Staff
                        
                        * Please Note that this will delete EVERYTHING. Proceed with caution
                        ** Please Note that this will DELETE EVERYTHING and generate NEW RECORDS. Proceed with caution.
                                :: '''))

                        # connection = sqlite3.connect(database_path)
                        # cursor = connection.cursor()
                        # cursor.execute('SELECT LoginID, Username, Permission, AccountStatus FROM LoginInformation;')
                        # userInfo = cursor.fetchall()
                        match AdminOption:
                            case 1:
                                print('Resetting Database in progress...')
                                setup_database()
                                print('Database successfully reset...')
                            case 2:
                                print('Resetting Database in progress...')
                                setup_database()
                                print('Database successfully reset...')

                                print('Generating New Database...')
                                GenerateDatabase(10)
                            # case 3:
                            #     AccountLoginID = int(input(f'''Select Account to Unlock by LoginID?
                            #     Accounts Available {userInfo}
                            #         :: '''))
                            #     updateAccount('Account', 'Unlocked', AccountLoginID)
                            #
                            # case 4:
                            #     AccountLoginID = int(input(f'''Select Account to sign up to STAFF By LoginID?
                            #         Accounts Available {userInfo}
                            #             :: '''))
                            #     updateAccount('Permission', 'Customer', AccountLoginID)

                    case _:
                        print('Invalid Option')
            if PermissionCheck(session.logUser) == 'Staff':
                match displayOptions():
                    case 1:
                        print('You have selected: Add Items to Inventory')
                        AddInventoryRun()
                    case 2:
                        print('You have selected: Modify System')
                        ModifyInventoryRun()

                    case 3:
                        print('You have selected: Check for low stocks')
                        GenerateAlert()
                    case 4:
                        print('You have selected: Track Shipment')
                        Inout = int(input('''Do you want to see Incoming or Outgoing Schedules?
                        [1] - Incoming
                        [2] - Outgoing'''))
                        getAllShipments(Inout)

                    case 5:
                        print('You have selected option 5')

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

# if userLoginSignup == 1:
#     print('resetting Database...')
#     setup_database()
#         # Insert Closing Logic

# -- OutgoingTransportationSchedules
# OutGoingScheduleID
# ExpectedArrivalDate
# IsItOnTheWay
# CustomerID
# PurchaseID
#
# -- Customer
# CustomerName
# CustomerAddress


