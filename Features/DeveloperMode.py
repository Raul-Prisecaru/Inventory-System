import sqlite3
import random

numbersNcharacters = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                      "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

with open("../TextFile/NameRecords.txt", "r") as file:
    nameList = []
    try:
        for line in file:
            nameList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: NameRecords.txt not found")

with open("../TextFile/LocationBuilding.txt", "r") as file:
    locationList = []
    try:
        for line in file:
            locationList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: LocationBuilding.txt not found")

with open("../TextFile/VehicleType.txt", "r") as file:
    VehicleTypeList = []
    try:
        for line in file:
            VehicleTypeList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: VehicleType.txt not found")

with open("../TextFile/VehicleBrand.txt", "r") as file:
    VehicleBrandList = []
    try:
        for line in file:
            VehicleBrandList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: VehicleBrand.txt not found")

with open("../TextFile/ExternalCompanies.txt", "r") as file:
    ExternalCompaniesList = []
    try:
        for line in file:
            ExternalCompaniesList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: ExternalCompanies.txt not found")


def numberGenerator(maxDigits):
    phoneNumber = "".join(str(random.randint(1, 9)) for _ in range(maxDigits))

    return "07" + phoneNumber


def licenseGenerator(maxLimit):
    license = "".join(str(random.choice(numbersNcharacters)) for _ in range(maxLimit))

    return license


def randomDate(startYear=2024, endYear=2025, startMonth=1, endMonth=12, startDay=1, endDate=30):
    Year = random.randint(startYear, endYear)
    Month = random.randint(startMonth, endMonth)
    Day = random.randint(startDay, endDate)
    return f"{Year}-{Month}-{Day}"


def randomTime(startHour=1, endHour=12, startMinute=1, endMinute=59):
    Hour = random.randint(startHour, endHour)
    Minute = random.randint(startMinute, endMinute)

    return f"{Hour}:{Minute}"


def randomiseInventory():
    try:
        connection = sqlite3.connect('../Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, LocationBuilding)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        for row in range(5):
            cursor.execute(select_query, (
           random.choice(nameList), random.randint(30, 400), random.choice(locationList)))


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
        connection = sqlite3.connect('../Database/CentralisedDatabase.db')
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
        connection = sqlite3.connect('../Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Vehicles(VehicleType, VehicleBrand, VehicleLicensePlate)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Vehicles;"

        for row in range(5):
            cursor.execute(select_query,
                           (random.choice(VehicleTypeList), random.choice(VehicleBrandList), licenseGenerator(7)))

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
        connection = sqlite3.connect('../Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO OutgoingTransportationSchedules(ExpectedArrivalDate, ExpectedArrivalTime, IsItOnTheWay)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM OutgoingTransportationSchedules;"

        for row in range(5):
            cursor.execute(select_query, (randomDate(), randomTime(), random.randint(0, 1)))

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
        connection = sqlite3.connect('../Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO IncomingTransportationSchedules(ExpectedArrivalDate, ExpectedArrivalTime, IsItOnTheWay)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM IncomingTransportationSchedules;"

        for row in range(5):
            cursor.execute(select_query, (randomDate(), randomTime(), random.randint(0, 1)))

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
        connection = sqlite3.connect('../Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO ExternalCompanies(ExternalCompanyName, ExternalCompanyRelationship)
            VALUES (?,?)
            """

        showcase_query = "SELECT * FROM ExternalCompanies;"

        with open("../TextFile/NameRecords.txt", "r") as file:
            for line in file:
                nameList.append(line)
                line.strip()

        with open("../TextFile/LocationBuilding.txt", "r") as file:
            for line in file:
                locationList.append(line)
                line.strip()

        for row in range(5):
            cursor.execute(select_query, (random.choice(ExternalCompaniesList), randomDate(1990, 2024)))

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


def countDatabase(column):
    numberRows = 0
    try:
        connection = sqlite3.connect('../Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        showcase_query = f"SELECT * FROM {column};"
        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            numberRows += 1

        cursor.close()
        connection.close()
        return numberRows
    except NameError:
        print(f"Error Caught: {column} not found")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))


def run():

    for row in range(100):
        randomiseInventory()
        randomiseDrivers()
        randomiseVehicles()
        randomiseIncomingTransportationSchedules()
        randomiseOutgoingTransportationSchedules()
        randomiseExternalCompanies()

run()