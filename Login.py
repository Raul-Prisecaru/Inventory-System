import sqlite3


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


def SignUp(username, password):
    connection = sqlite3.connect("Database/CentralisedDatabase.db")
    cursor = connection.cursor()

    cursor.execute('INSERT INTO LoginInformation VALUES (?,?)', (username, password))
    connection.commit()
    connection.close()



if __name__ == '__main__':
    # if Login('asd', 'Password'):
    #     print("Login Successful")
    # else:
    #     print("Login Failed")
    SignUp('Jake', '123')