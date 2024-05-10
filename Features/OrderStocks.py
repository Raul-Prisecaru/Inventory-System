import sqlite3
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def orderStocks(ID, Stock):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM ExternalCompanies")
    EC = cursor.fetchall()
    ECList = []
    for row in EC:
        ECList.append(row[0])
        print(f'''
        External Company ID: {row[0]}
        External Company Name: {row[1]}
        ------Next Company--------
        ''')

    while True:
        ExternalCompID = int(input('''Select An ID you wish to book more Stocks From: '''))
        if ExternalCompID not in ECList:
            print('External Company Not Found')

        else:
            print('Company Found, Continue')
            cursor.execute('''INSERT INTO IncomingTransportationSchedules (IncomingStock, IsItOnTheWay, InventoryID, ExternalCompanyID)
                            VALUES (?,?,?,?)''', (Stock, 0, ID, ExternalCompID))

            connection.commit()
            IncomingID = cursor.lastrowid
            print(IncomingID)
            cursor.execute('SELECT * FROM viewDisplayIncomingSchedules WHERE IncomingScheduleID = ?', (IncomingID, ))
            order = cursor.fetchall()

            for row in order:
                print(f'''Your order has been successful:
                Incoming Schedule ID: {row[0]}
                Expected Delivery Date: {row[1]}
                Incoming Stocks: {row[2]}
                Is it on the way?: {'Yes' if row[3] == 1 else 'No'}
                InventoryID: {row[4]}
                External CompanyID: {row[5]}
                External Company Name: {row[7]}
                ''')

            break


