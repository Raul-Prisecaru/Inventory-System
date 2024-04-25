import sqlite3
import os
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
        connection.close()

        if loginInfo and loginInfo[0] == password:
            print("Login Successful...")
            return True
        else:
            print("Incorrect Username or Password...")
            return False
    except Exception as e:
        print(f"Unable to Login: {e}")
        return False


def SignUp(username, password):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute('INSERT INTO LoginInformation VALUES (?,?)', (username, password))
        connection.commit()
        connection.close()

        return True

    except Exception as e:
        print(f"Unable to Sign up: {e}")
        return False



if __name__ == '__main__':
    # if Login('asd', 'Password'):
    #     print("Login Successful")
    # else:
    #     print("Login Failed")
    pass