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

        with open("Database/CentralisedDatabase.sql", "r") as sql_file:
            sql_script = sql_file.read()

        cursor.executescript(sql_script)

        connection.commit()
        connection.close()
        print("Database Successfully Created")

    except NameError:
        print("NameError Caught: Database (.db) Not Found.")
    except Exception as e:
        print("Error Caught: " + str(e))


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
