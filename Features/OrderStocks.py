import sqlite3
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def orderStocks(ID):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM ExternalCompanies")
    EC = cursor.fetchall()

    for row in EC:
        print(f'''
        External Company ID: {row[0]}
        External Company Name: {row[0]}
        ------Next Company--------
        ''')

    ExternalCompID = int(input('Select An ID you wish to book more Stocks From'))

    cursor.execute('''INSERT INTO IncomingTransportationSchedules (IsItOnTheWay, InventoryID, ExternalCompanyID)
                    VALUES (?,?,?)''', (0, ID, ExternalCompID))

    cursor.execute('SELECT * FROM IncomingTransportationSchedules;')
    rows = cursor.fetchall()

    for row in rows:
        print('Incoming Schedules')
        print(row)
    connection.commit()

