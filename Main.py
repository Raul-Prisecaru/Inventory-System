from TUI.AddInventoryTUI import run as AddInventoryRun
from TUI.ModifyInventoryTUI import run as ModifyInventoryRun
from Features.Login import *
from Features.GenerateLogs import addToLogs, displayLogs
from Features.TrackShipment import getAllShipments
from Features.DeveloperMode import run as GenerateDatabase
import os


# Get the directory of the current script file
current_directory = os.path.dirname(__file__)


# Construct the path to the database file relative to the current directory
# database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')
# sql_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.sql')


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
    userInput = int(input("""Welcome to St Mary's Inventory System
        What would you like to do?
            [0] - Guidebook to using the System
            [1] - Add To Inventory
            [2] - Temporarily Unavailable
            [3] - Modify Inventory
            [4] - Track All Shipments
            [5] - View Inventory
            [6] - View Logs
            [7] - Admin | Reset Database
                :: """))

    return userInput


userLoginSignup = int(input('''Do you want to:
[1] - Login
[2] - Signup
[3] - Exit
    :: '''))
username = str(input('Enter Your Username: '))
password = str(input('Enter Your Password: '))

if __name__ == '__main__':
    if userLoginSignup == 1:
        if Login(username, password):
            print('Login Successful')
            match displayOptions():
                case 0:
                    with open('TextFile/StaffIntroductionSystem.txt', 'r') as File:
                        for line in File:
                            print(line, end='')
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
                    [3] - Lock/Unlock Account
                    
                    * Please Note that this will delete EVERYTHING. Proceed with caution
                    ** Please Note that this will DELETE EVERYTHING and generate NEW RECORDS. Proceed with caution.'''))

                    match AdminOption:
                        case 1:
                            print('Resetting Database in progress...')
                            setup_database()
                            print('Database successfully reset...')
                        case 2:
                            print('Deleting Database...')
                            setup_database()
                            print('Generating New Database')
                            GenerateDatabase()

                case _:
                    print('Invalid Option')
    elif userLoginSignup == 2:
        SignUp(username, password)
    elif userLoginSignup == 3:
        print('Exiting...')
        # Insert Closing Logic
