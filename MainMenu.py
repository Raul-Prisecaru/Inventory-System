import sqlite3
import tkinter as tk
from DeveloperMode import countDatabase
from AddNewInventory import getAllColumns as displayAllColumns
from AddNewInventory import addToInventory

userInput = int(input("""Welcome to St Mary's Logistic System:
    What would you like to do?
        [1] Add new Inventory
        [2] Modify Inventory
        [3] Track Shipments
        [4] Generate Report
        [5] Introduction To System.
        [6] Quit
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
    match userInput:
        case 1:
            print("You have selected option 1")
            try:
                valueStrip = []
                selectTable = str(input("What table do you want to add?"))
                tableColumns = str(input(f"""Enter in this format: {displayAllColumns(selectTable)}
                    :: """))
                # Take the User Input and Split it accordingly to be used for the  table placeholders
                splitColumns = tableColumns.split(",")

                # Do a ForLoop to strip any WhiteSpace in the User Answer
                for value in splitColumns:
                    valueStrip.append(value.strip())

                # Arguments: {Table}, {Placeholder Answers}.
                addToInventory(selectTable, valueStrip)
            except Exception as e:
                print(f"Something went wrong: {e}")
        case 2:
            print("You have selected option 2")
        case 3:
            print("You have selected option 3")
        case 4:
            print("You have selected option 4")
        case 5:
            print("You have selected option 5")
        case 6:
            print("You have selected option 6")
        case _:
            print("Invalid option")

# 4000, "Google", 400, "London", 123
