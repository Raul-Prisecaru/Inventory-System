import sqlite3
import random
import timeit
import os

numbersNcharacters = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                      "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
databasePath = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')
sqlPath = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.sql')
nameRecordPath = os.path.join(current_directory, '..', 'TextFile', 'NameRecords.txt')
InventoryPath = os.path.join(current_directory, '..', 'TextFile', 'InventoryItems.txt')
locationBuildingPath = os.path.join(current_directory, '..', 'TextFile', 'LocationBuilding.txt')
vehicleBrandPath = os.path.join(current_directory, '..', 'TextFile', 'VehicleBrand.txt')
vehicleTypePath = os.path.join(current_directory, '..', 'TextFile', 'VehicleType.txt')
externalCompaniesPath = os.path.join(current_directory, '..', 'TextFile', 'ExternalCompanies.txt')
print(f'databasepath: {databasePath}')

with open(nameRecordPath, "r") as file:
    nameList = []
    try:
        for line in file:
            nameList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: NameRecords.txt not found")

with open(InventoryPath, "r") as file:
    inventoryList = []
    try:
        for line in file:
            inventoryList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: File not found")

with open(locationBuildingPath, "r") as file:
    locationList = []
    try:
        for line in file:
            locationList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: LocationBuilding.txt not found")

with open(vehicleTypePath, "r") as file:
    VehicleTypeList = []
    try:
        for line in file:
            VehicleTypeList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: VehicleType.txt not found")

with open(vehicleBrandPath, "r") as file:
    VehicleBrandList = []
    try:
        for line in file:
            VehicleBrandList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: VehicleBrand.txt not found")

with open(externalCompaniesPath, "r") as file:
    ExternalCompaniesList = []
    try:
        for line in file:
            ExternalCompaniesList.append(line)
            line.strip()
    except IOError:
        print("Error Caught: ExternalCompanies.txt not found")


def EmailGenerator():
    EndEmail = ['.com', '.ac.uk', '.edu', '.uk', '.co']
    EmailProviders = ['Outlook', 'Yahoo', 'Protonmail', 'Gmail', 'Zoho']
    firstnameRandom = random.choice(nameList)
    lastnameRandom = random.choice(nameList)
    EmailProvidersRandom = random.choice(EmailProviders)
    EndEmailRandom = random.choice(EndEmail)

    return f'{firstnameRandom}.{lastnameRandom}@{EmailProvidersRandom}{EndEmailRandom}'


def AddressGenerator():
    FirstPart = ['Caxton', 'Southlands', '.Carriers', 'Bootham', 'Grey']
    LastPart = ['Place', 'Road', 'Crescent', 'Street', 'St']
    FirstPartRandom = random.choice(nameList)
    LastPartRandom = random.choice(nameList)
    AddressNumber = "".join(str(random.randint(1, 9)) for _ in range(3))

    return f'{AddressNumber} {FirstPartRandom} {LastPartRandom}'


def numberGenerator(maxDigits):
    phoneNumber = "".join(str(random.randint(1, 9)) for _ in range(maxDigits))

    return "07" + phoneNumber


def creditcardGenerator():
    creditcard = "".join(str(random.randint(1, 9)) for _ in range(16))
    return creditcard


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


def randomiseLoginAndCustomer():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()

        Customer_query = """
            INSERT INTO Customer(CustomerName, CustomerEmail, CustomerAddress, CustomerPhoneNumber, CustomerCreditCard)
            VALUES (?,?,?,?,?)
            """
        # Generate values for Customer table
        customer_values = (
        random.choice(nameList), EmailGenerator(), AddressGenerator(), numberGenerator(11), creditcardGenerator())

        cursor.execute(Customer_query, customer_values)

        # Retrieve the last inserted CustomerID
        CustomerID = cursor.lastrowid

        Login_query = """
            INSERT INTO LoginInformation(Username, Password, Permission, AccountStatus, CustomerID)
            VALUES (?,?,?,?,?)
            """

        # Generate values for LoginInformation table
        login_values = (licenseGenerator(6), licenseGenerator(6), random.choice(('Staff', 'Customer')),
                        random.choice(('Unlocked', 'Locked')), CustomerID)

        cursor.execute(Login_query, login_values)
        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In LoginAndCustomer: " + str(e))


def randomiseInventory():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, InventoryPrice, LocationBuilding)
            VALUES (?,?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        randomFloat = random.uniform(1, 1000)
        randomFloatRounded = round(randomFloat, 2)

        cursor.execute(select_query, (
            random.choice(inventoryList), random.randint(30, 400), randomFloatRounded, random.choice(locationList)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In Inventory: " + str(e))


def randomisePurchases():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()

        # Randomise Customer Foreign
        cursor.execute('SELECT CustomerID FROM Customer')
        CustomerList = []
        CustomerCursor = cursor.fetchall()

        for row in CustomerCursor:
            CustomerList.append(row)
        Customerrand = random.choice(CustomerList)

        # Randomise Inventory Names
        cursor.execute('SELECT InventoryName FROM Inventory')
        InventoryList = []
        InventoryCursor = cursor.fetchall()

        for row in InventoryCursor:
            InventoryList.append(row)
        Inventoryrand = random.choice(InventoryList)

        select_query = """
            INSERT INTO Purchase(PurchaseName, PurchaseDeliveryDate, PurchaseStock, CustomerID)
            VALUES (?,?,?,?)
            """

        showcase_query = "SELECT * FROM Purchase;"

        randomFloat = random.uniform(1, 1000)
        randomFloatRounded = round(randomFloat, 2)

        cursor.execute(select_query, (
            Inventoryrand[0], randomDate(), random.randint(1, 999), Customerrand[0]))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In Purchase: " + str(e))


def randomiseDrivers():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Drivers(DriverName, DriverPhoneNumber, DriverLicenseRegistrationID)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Drivers;"

        cursor.execute(select_query, (random.choice(nameList), numberGenerator(10), licenseGenerator(16)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In Drivers: " + str(e))


def randomiseVehicles():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()
        cursor.execute('SELECT DriverID FROM Drivers')
        DriversList = []
        DriverCursor = cursor.fetchall()

        for row in DriverCursor:
            DriversList.append(row)

        Driverrand = random.choice(DriversList)

        select_query = """
            INSERT INTO Vehicles(VehicleType, VehicleBrand, VehicleLicensePlate, DriverID)
            VALUES (?,?,?,?)
            """

        showcase_query = "SELECT * FROM Vehicles;"

        cursor.execute(select_query,
                       (random.choice(VehicleTypeList), random.choice(VehicleBrandList), licenseGenerator(7),
                        Driverrand[0]))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In Vehicles: " + str(e))


def randomiseOutgoingTransportationSchedules():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()
        # Randomise Customer Foreign
        cursor.execute('SELECT CustomerID FROM Customer')
        CustomerList = []
        CustomerCursor = cursor.fetchall()

        for row in CustomerCursor:
            CustomerList.append(row)
        Customerrand = random.choice(CustomerList)

        # Randomise Purchase Foreign
        cursor.execute('SELECT PurchaseID FROM Purchase')
        PurchaseList = []
        PurchaseCursor = cursor.fetchall()

        for row in PurchaseCursor:
            PurchaseList.append(row)
        Purchaserand = random.choice(PurchaseList)

        # Randomise Driver Foreign
        cursor.execute('SELECT DriverID FROM Drivers')
        DriversList = []
        DriverCursor = cursor.fetchall()

        for row in DriverCursor:
            DriversList.append(row)
        Driverrand = random.choice(DriversList)

        select_query = """
            INSERT INTO OutgoingTransportationSchedules(ExpectedArrivalDate, IsItOnTheWay, CustomerID, PurchaseID, DriverID)
            VALUES (?,?,?,?,?)
            """

        showcase_query = "SELECT * FROM OutgoingTransportationSchedules;"

        cursor.execute(select_query,
                       (randomDate(), random.randint(0, 1), Customerrand[0], Purchaserand[0], Driverrand[0]))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In Outgoing Schedules: " + str(e))


def randomiseIncomingTransportationSchedules():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()

        # Randomise Inventory Foreign
        cursor.execute('SELECT InventoryID FROM Inventory')
        InventoryList = []
        InventoryCursor = cursor.fetchall()

        for row in InventoryCursor:
            InventoryList.append(row)
        Inventoryrand = random.choice(InventoryList)

        # Randomise ExternalCompany Foreign
        cursor.execute('SELECT ExternalCompanyID FROM ExternalCompanies')
        ExternalCompanyList = []
        ExternalCompanyCursor = cursor.fetchall()

        for row in ExternalCompanyCursor:
            ExternalCompanyList.append(row)
        ExternalCompanyrand = random.choice(ExternalCompanyList)

        select_query = """
            INSERT INTO IncomingTransportationSchedules(ExpectedArrivalDate, IncomingStock, IsItOnTheWay, InventoryID, ExternalCompanyID)
            VALUES (?,?,?,?,?)
            """

        showcase_query = "SELECT * FROM IncomingTransportationSchedules;"

        cursor.execute(select_query, (
            randomDate(), random.randint(1, 1000), random.randint(0, 1), Inventoryrand[0], ExternalCompanyrand[0]))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In Incoming Schedules: " + str(e))


def randomiseExternalCompanies():
    try:
        connection = sqlite3.connect(databasePath)
        cursor = connection.cursor()

        select_query = """
            INSERT INTO ExternalCompanies(ExternalCompanyName, ExternalCompanyRelationship)
            VALUES (?,?)
            """

        showcase_query = "SELECT * FROM ExternalCompanies;"

        with open(nameRecordPath, "r") as file:
            for line in file:
                nameList.append(line)
                line.strip()

        with open(locationBuildingPath, "r") as file:
            for line in file:
                locationList.append(line)
                line.strip()

        cursor.execute(select_query, (random.choice(ExternalCompaniesList), randomDate(1990, 2024)))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except Exception as e:
        print("Something Else Went Wrong In ExternalCompanies: " + str(e))


def countDatabase(column):
    numberRows = 0
    try:
        connection = sqlite3.connect(databasePath)
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


def run(repeat=1):
    # start_time = timeit.default_timer()

    for row in range(repeat):
        randomiseInventory()
        randomiseLoginAndCustomer()
        randomisePurchases()
        randomiseDrivers()
        randomiseVehicles()
        randomiseIncomingTransportationSchedules()
        randomiseOutgoingTransportationSchedules()
        randomiseExternalCompanies()

    # end_time = timeit.default_timer()
    # return end_time - start_time

# time_taken = timeit.timeit(stmt="run(10)", setup="from __main__ import run", number=1)
# print("Time taken:", time_taken)
