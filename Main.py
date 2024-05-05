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
                [7] - Admin | Reset Database
                    :: """))
    elif PermissionCheck(session.logUser) == 'Staff':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Add To Inventory
                [2] - Temporarily Unavailable
                [3] - Modify Inventory
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

setup_database()
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
                        
                        * Please Note that this will delete EVERYTHING. Proceed with caution
                        ** Please Note that this will DELETE EVERYTHING and generate NEW RECORDS. Proceed with caution.
                                :: '''))

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
                            case 3:
                                print(session.logUser)
                                connection = sqlite3.connect(database_path)
                                cursor = connection.cursor()
                                cursor.execute('SELECT Username FROM LoginInformation;')
                                rows = cursor.fetchall()
                                AccountModification = str(input(f'''Which account do you want to unlock?
                                Accounts Available {rows}
                                    :: '''))
                                username = session.logUser
                                print(username)
                                sql_query = f"UPDATE LoginInformation SET AccountStatus = 'Unlocked' WHERE Username = ?"
                                cursor.execute(sql_query, (AccountModification,))
                                connection.commit()
                                connection.close()

                    case _:
                        print('Invalid Option')
            if PermissionCheck(session.logUser) == 'Staff':
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

                    case _:
                        print('Invalid Option')

            if PermissionCheck(session.logUser) == 'Customer':
                match displayOptions():
                    case 1:
                        print('You have selected: Purchase Inventory')
                        PurchaseInventoryRun()

                    case 2:
                        print('Option 2')

                    case _:
                        print('Invalid Option')

    elif userLoginSignup == 2:
        CustomerName = str(input('Enter Your Name: '))
        CustomerEmail = str(input('Enter Your Email: '))
        CustomerAddress = str(input('Enter Your Address: '))
        CustomerPhoneNumber = int(input('Enter Your Phone Number: '))
        CustomerCreditCard = int(input('Enter Your Long Credit Card: '))
        SignUp(username, password, CustomerName, CustomerEmail, CustomerAddress, CustomerPhoneNumber, CustomerCreditCard)
    elif userLoginSignup == 3:
        print('Exiting...')


# if userLoginSignup == 1:
#     print('resetting Database...')
#     setup_database()
#         # Insert Closing Logic
