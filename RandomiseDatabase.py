import sqlite3
import random

nameList = []
locationList = []

def randomiseInventory():
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
            cursor.execute(select_query, (random.choice(nameList), random.randint(30, 400), random.choice(locationList)))

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
    randomiseInventory()