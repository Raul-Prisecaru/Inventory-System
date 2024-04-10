import sqlite3
LogisticSystemOption = int(input("""Welcome to St Mary's Logistic System
What would you like to do?
[1] - Add New Inventory
[2] - Manage Inventory
[3] - Track All Shipment
[4] - Generate Reports for Inventory Status
:: """))

def setup_database():
    try:
        connection = sqlite3.connect("Database/CentralisedDatabase.db")
        cursor = connection.cursor()

        with open("Database/CentralisedDatabase.sql", "r") as CentralisedDatabaseFile:
            sql_script = CentralisedDatabaseFile.read()

        cursor.execute(sql_script)

        connection.commit()
        connection.close()
    except NameError:
        print("NameError Caught: Database (.db) Not Found.")
    except:
        print("Error Caught: Database (.db) Accessable but couldn't execute SQL")


if __name__ == '__main__':
    match LogisticSystemOption:
        case 1:
            print("You have selected 1")
            setup_database()
        case 2:
            print("You have selected 2")

        case 3:
            print("You have selected 3")

        case 4:
            print("You have selected 4")

        case _:
            print("Invalid Option was selected")
