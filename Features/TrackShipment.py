import sqlite3
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def getAllShipments(number):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    # cursor.execute(f'''SELECT IncomingTransportationSchedules.IncomingScheduleID,
    #                     IncomingTransportationSchedules.ExpectedArrivalDate,
    #                     IncomingTransportationSchedules.ExpectedArrivalTime,
    #                     OutgoingTransportationSchedules.OutgoingScheduleID,
    #                     OutgoingTransportationSchedules.ExpectedArrivalDate,
    #                     OutgoingTransportationSchedules.ExpectedArrivalTime
    #                     FROM IncomingTransportationSchedules
    #                     CROSS JOIN OutgoingTransportationSchedules''')
    if number == 1:
        cursor.execute('SELECT * FROM viewDisplayIncomingSchedules;')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
            print(f''' INCOMING SCHEDULES:
                    Schedule ID: {row[0]}
                    Schedule Date: {row[1]}
                    Is it on the way?: {'Yes' if row[2] == 1 else 'No'}
                    InventoryID: {row[3]}
                    ExternalCompanyID: {row[4]}
                    External Company Name: {row[5]}
                    Relationship Date: {row[6]}
                    ---------Next Item----------''')

        connection.commit()
        connection.close()
    elif number == 2:
        cursor.execute('SELECT * FROM viewDisplayOutgoingSchedules;')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
            print(f'''
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

        connection.commit()
        connection.close()


# getAllShipments(1)
