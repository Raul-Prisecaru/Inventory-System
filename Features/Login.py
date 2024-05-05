import sqlite3
import os

from Features.GenerateLogs import addToLogs

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


# def displayInformation():
#     connection = sqlite3.connect(database_path)
#     cursor = connection.cursor()
#
#     cursor.execute('SELECT * FROM masked_Customer')
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print(row)


def Login(username, password):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute('SELECT Password FROM LoginInformation WHERE Username = ?', (username,))
        loginInfo = cursor.fetchone()

        cursor.execute('SELECT Username FROM LoginInformation WHERE AccountStatus = "Locked" AND Username = ?',
                       (username,))
        LockedAccounts = cursor.fetchone()

        if LockedAccounts:
            print(f'{username} is Locked')
            return False

        if loginInfo and loginInfo[0] == password:
            print("Login Successful...")
            # addToLogs(username, f'{username} has successfully logged in')
            return True
        else:
            print("Incorrect Username or Password...")
            # addToLogs(username, f'{username} has failed to log in')
            return False

    except Exception as e:
        print(f"Unable to Login: {e}")
        return False


def SignUp(username, password, Name, Email, Address, PhoneNumber, CreditCard):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute('INSERT INTO LoginInformation (Username, Password) VALUES (?,?)', (username, password))
        cursor.execute('''INSERT INTO Customer (CustomerName, CustomerEmail, CustomerAddress, CustomerPhoneNumber, CustomerCreditCard) 
                                VALUES (?,?,?,?,?)''', (Name, Email, Address, PhoneNumber, CreditCard))
        connection.commit()
        connection.close()
        # addToLogs(username, f'{username} has successfully signed up to the system')
        return True

    except Exception as e:
        print(f"Unable to Sign up: {e}")
        # addToLogs(username, f'{username} has failed to Sign Up due to error')
        return False
