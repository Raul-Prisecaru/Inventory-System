import sqlite3


def randomiseDatabase():
    try:
        connection = sqlite3.connect('Database/CentralisedDatabase.db')
        cursor = connection.cursor()

        select_query = """
            INSERT INTO Inventory(InventoryName, StockLevel, LocationBuilding)
            VALUES (?,?,?)
            """

        showcase_query = "SELECT * FROM Inventory;"

        for row in range(1000):
            cursor.execute(select_query, ("asd", 123, "dfg"))

        cursor.execute(showcase_query)

        connection.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except NameError:
        print("Error Caught: Database Not Found.")
    except Exception as e:
        print("Something Else Went Wrong: " + str(e))

if __name__ == '__main__':
    randomiseDatabase()