from TUI.AddInventoryTUI import run as AddInventoryRun
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
    elif PermissionCheck(session.logUser) == 'ExternalCompany':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Track Outgoing Shipments
                    :: """))

    elif PermissionCheck(session.logUser) == 'Driver':
        userInput = int(input("""Welcome to St Mary's Inventory System
            What would you like to do?
                [1] - Display Your Information
                [2] - View your task
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

            if PermissionCheck(session.logUser) == 'ExternalCompany':
                match displayOptions():
                    case 1:
                        print('Option 1')

                    case 2:
                        print('Maybe add Requests from Internal Company')

            if PermissionCheck(session.logUser) == 'Driver':
                match displayOptions():
                    case 1:
                        print('Option 1')

                    case 2:
                        print('Option 2')

    elif userLoginSignup == 2:
        SignUp(username, password)
    elif userLoginSignup == 3:
        print('Exiting...')
    elif userLoginSignup == 4:
        print('resetting Database...')
        setup_database()
        # Insert Closing Logic
