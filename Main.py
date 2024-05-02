from TUI.AddInventoryTUI import run as AddInventoryRun
from TUI.ModifyInventoryTUI import run as ModifyInventoryRun
from Features.Login import *
from Features.GenerateLogs import addToLogs, displayLogs
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
            [0] - Reset Database
            [1] - Add Items to Inventory
            [2] - Add Stock to Inventory
            [3] - Modify System
            [4] - Track Shipments
            [5] - View Database
            [6] - View Logs
            [7] - Admin
                :: """))

    return userInput


userLoginSignup = int(input('''Do you want to:
[1] - Login
[2] - Signup'''))
username = str(input('Enter Your Username: '))
password = str(input('Enter Your Password: '))

if __name__ == '__main__':
    if userLoginSignup == 1:
        if Login(username, password):
            print('Login Successful')
            match displayOptions():
                case 0:
                    print('Resetting Database in progress...')
                    setup_database()
                    print('Database successfully reset...')
                case 1:
                    print('You have selected: Add Items to Inventory')
                    AddInventoryRun()
                case 2:
                    print('You have selected option 2')

                case 3:
                    print('You have selected: Modify System')
                    ModifyInventoryRun()

                case 4:
                    print('You have selected option 4')

                case 5:
                    print('You have selected option 5')

                case 6:
                    print('You have selected: View Logs')
                    displayLogs()

                case 7:
                    pass

                case _:
                    print('Invalid Option')
    else:
        SignUp(username, password)
