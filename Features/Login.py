import sqlite3
import os

import Features.session as session

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

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
            session.setlogUser(username)
            return True
        else:
            print("Incorrect Username or Password...")
            return False

    except Exception as e:
        print(f"Unable to Login: {e}")
        return False


def SignUp(username, password, Name, Email, Address, PhoneNumber, CreditCard):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute('''INSERT INTO Customer (CustomerName, CustomerEmail, CustomerAddress, CustomerPhoneNumber, CustomerCreditCard) 
                                VALUES (?,?,?,?,?)''', (Name, Email, Address, PhoneNumber, CreditCard))
        CustomerID = cursor.lastrowid

        cursor.execute('''INSERT INTO LoginInformation (Username, Password, CustomerID) 
                                VALUES (?,?,?)''', (username, password, CustomerID))

        connection.commit()
        connection.close()
        return True

    except Exception as e:
        print(f"Unable to Sign up: {e}")
        return False



