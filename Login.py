import sqlite3


def SignUp(Table, Query1='Admin', Query2='Password'):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    # executeQuery = f"INSERT INTO {Table} (Username, Password) VALUES (?,?)"
    # cursor.execute(executeQuery, (Query1, Query2))


def Login(username, password):
    connection = sqlite3.connect('Database/CentralisedDatabase.db')
    cursor = connection.cursor()

    cursor.execute('SELECT Password FROM LoginInformation WHERE Username = ?', (username,))
    loginInfo = cursor.fetchone()
    connection.close()

    if loginInfo and loginInfo[0] == password:
        return True
    else:
        return False


if __name__ == '__main__':
    if Login('asd', 'Password'):
        print("Login Successful")
    else:
        print("Login Failed")
