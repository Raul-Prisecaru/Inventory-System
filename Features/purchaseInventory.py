import random
import sqlite3
import os

import Features.session as session

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


def getCustomerID():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    # Come back to this
    cursor.execute(f'SELECT CustomerID FROM LoginInformation WHERE Username = ?', (session.logUser,))
    CustomerID = cursor.fetchone()

    return CustomerID[0]


def CustomerPurchase(ID, Stock):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Update StocksLevel from Inventory Table with the amount of stocks chosen by user.
    cursor.execute(f"""UPDATE Inventory 
        SET StockLevel = StockLevel - {Stock} 
        WHERE InventoryID = {ID}""")

    # Commit and Close Connection
    connection.commit()
    connection.close()


def confirmationPurchase(ID, Stock):
    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Prepare the query with placeholders for variables
    cursor.execute(f'''
        SELECT 
            InventoryID,
            InventoryName,
            InventoryPrice * {Stock} AS FormattedPrice,
            StockLevel
        FROM 
            Inventory 
        WHERE 
            InventoryID = {ID}
    ''')

    # Fetch the result
    confirmation = cursor.fetchone()

    if confirmation:
        inventory_id, inventory_name, total_price, stock_level_check = confirmation
        stock_level = stock_level_check
        if stock_level <= 0:
            print("Error: No stock available \n")
            return False

        userConfirmation = int(input(f'''Do you want to proceed?
        Inventory ID: {inventory_id} 
        Inventory Name: {inventory_name}
        Total Price: {total_price}                          

        [1] - Proceed
        [2] - Cancel
        :: '''))

        if userConfirmation == 1:
            DriversList = []
            cursor.execute('SELECT DriverID FROM Drivers;')
            Driver = cursor.fetchall()

            for row in Driver:
                DriversList.append(row)

            randomDriver = random.choice(DriversList)

            cursor.execute("INSERT INTO Purchase (PurchaseName, PurchaseStock, CustomerID) VALUES (?,?,?)",
                           (inventory_name, Stock, getCustomerID()))

            PurchaseID = cursor.lastrowid

            cursor.execute("""INSERT INTO OutgoingTransportationSchedules (IsItOnTheWay, CustomerID, PurchaseID, DriverID) 
                                    VALUES (?,?,?,?)""",
                        (0, getCustomerID(), PurchaseID, randomDriver[0]))

            connection.commit()
            connection.close()
            return True
        else:
            connection.close()
            return False
