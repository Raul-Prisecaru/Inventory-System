import sqlite3
import random

nameList, locationList = [], []
numbersNcharacters = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                      "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

with open("TextFile/NameRecords.txt", "r") as file:
    try:
        for line in file:
            nameList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: NameRecords.txt not found")

with open("TextFile/LocationBuilding.txt", "r") as file:
    try:
        for line in file:
            locationList.append(line)
            line.strip()
    except IOError:
        print("Error Caught:LocationBuilding.txt not found")

def numberGenerator(maxDigits):
        phoneNumber = "".join(str(random.randint(1, 9)) for _ in range(maxDigits))

        return "07" + phoneNumber

def licenseGenerator(maxLimit):
    license = "".join(str(random.choice(numbersNcharacters))for _ in range(maxLimit))

    return license
def randomiseInventory():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, LocationBuilding)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        for row in range(5):
            cursor.execute(select_query,(random.choice(nameList), random.randint(30, 400), random.choice(locationList)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except NameError:
        print("Error Caught: File Not Found.")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))


def randomiseDrivers():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Drivers(DriverName, DriverPhoneNumber, DriverLicenseRegistrationID)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Drivers;"

        for row in range(5):
            cursor.execute(select_query, (random.choice(nameList), numberGenerator(10), licenseGenerator(16)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except NameError:
        print("Error Caught: File Not Found.")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))


def randomiseVehicles():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, LocationBuilding)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        with open("TextFile/NameRecords.txt", "r") as file:
            for line in file:
                nameList.append(line)
                line.strip()

        with open("TextFile/LocationBuilding.txt", "r") as file:
            for line in file:
                locationList.append(line)
                line.strip()

        for row in range(5):
            cursor.execute(select_query,
                           (random.choice(nameList), random.randint(30, 400), random.choice(locationList)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except NameError:
        print("Error Caught: File Not Found.")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))


def randomiseOutgoingTransportationSchedules():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, LocationBuilding)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        with open("TextFile/NameRecords.txt", "r") as file:
            for line in file:
                nameList.append(line)
                line.strip()

        with open("TextFile/LocationBuilding.txt", "r") as file:
            for line in file:
                locationList.append(line)
                line.strip()

        for row in range(5):
            cursor.execute(select_query,
                           (random.choice(nameList), random.randint(30, 400), random.choice(locationList)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except NameError:
        print("Error Caught: File Not Found.")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))


def randomiseIncomingTransportationSchedules():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, LocationBuilding)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        with open("TextFile/NameRecords.txt", "r") as file:
            for line in file:
                nameList.append(line)
                line.strip()

        with open("TextFile/LocationBuilding.txt", "r") as file:
            for line in file:
                locationList.append(line)
                line.strip()

        for row in range(5):
            cursor.execute(select_query,
                           (random.choice(nameList), random.randint(30, 400), random.choice(locationList)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except NameError:
        print("Error Caught: File Not Found.")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))


def randomiseExternalCompanies():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, LocationBuilding)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        with open("TextFile/NameRecords.txt", "r") as file:
            for line in file:
                nameList.append(line)
                line.strip()

        with open("TextFile/LocationBuilding.txt", "r") as file:
            for line in file:
                locationList.append(line)
                line.strip()

        for row in range(5):
            cursor.execute(select_query,
                           (random.choice(nameList), random.randint(30, 400), random.choice(locationList)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except NameError:
        print("Error Caught: File Not Found.")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))


if __name__ == '__main__':
    randomiseDrivers()
