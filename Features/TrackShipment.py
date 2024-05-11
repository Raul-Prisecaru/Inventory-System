import sqlite3
import os

from Features import session
from Features.DisplayLogs import addToLogs

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

# Function Responsible for Getting all Shipment Information
def getAllShipments(number):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # If user picked 1 as argument then display Incoming Transportation Information
    if number == 1:
        # Get all Information from view
        cursor.execute('SELECT * FROM viewDisplayIncomingSchedules;')
        rows = cursor.fetchall()
        addToLogs(f'{session.logUser} has checked for incoming Shipment')
        # Display and format the information into user-readable
        for row in rows:
            print(f''' INCOMING SCHEDULES:
                    Schedule ID: {row[0]}
                    Schedule Date: {row[1]}
                    Is it on the way?: {'Yes' if row[3] == 1 else 'No'}
                    InventoryID: {row[4]}
                    ExternalCompanyID: {row[5]}
                    External Company Name: {row[7]}
                    ---------Next Item----------''')

        connection.close()

    # If user picked 2 as argument then display Outgoing Transportation Information
    elif number == 2:
        # Get all Information from view
        cursor.execute('SELECT * FROM viewDisplayOutgoingSchedules;')
        rows = cursor.fetchall()
        addToLogs(f'{session.logUser} has checked for outgoing shipment')
        # Display and format the information into user-readable
        for row in rows:
            print(f'''OUTGOING SCHEDULES:
            Schedule ID: {row[0]}
            Schedule Date: {row[1]}
            Is it on the way?: {'Yes' if row[2] == 1 else 'No'}
            CustomerID: {row[3]}
            PurchaseID: {row[4]}
            DriverID: {row[5]}
            DriverName: {row[7]}
            Customer Name: {row[8]}
            Delivery Address: {row[9]}
            Contact Number: {row[10]}
            ---------Next Item----------''')
        connection.close()


