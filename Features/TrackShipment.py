import sqlite3
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def getAllShipments():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(f'''SELECT IncomingTransportationSchedules.IncomingScheduleID, 
                        IncomingTransportationSchedules.ExpectedArrivalDate, 
                        IncomingTransportationSchedules.ExpectedArrivalTime,
                        OutgoingTransportationSchedules.OutgoingScheduleID, 
                        OutgoingTransportationSchedules.ExpectedArrivalDate,
                        OutgoingTransportationSchedules.ExpectedArrivalTime
                        FROM IncomingTransportationSchedules
                        CROSS JOIN OutgoingTransportationSchedules''')

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.commit()
    connection.close()



