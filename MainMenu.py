import sqlite3
import tkinter as tk
from DeveloperMode import countDatabase
from AddNewInventory import getAllColumns as displayAllColumns
from AddNewInventory import addToInventory
from ModifyInventory import modifyAllInventory, getAllColumnsNoID as displayAllColumnsModify


def run():
    window = MainWindowConfig()
    addComponents(window)
    window.mainloop()


def MainWindowConfig():
    window = tk.Tk()
    window.geometry('600x500')
    window.title("St Mary's University Inventory System")
    return window


def LoginPage(window):
    loginLabel = tk.Label(window, text="Username: ")
    loginLabel.pack()
    loginEntry = tk.Entry(window)
    loginEntry.pack()

    passwordLabel = tk.Label(window, text="Password: ")
    passwordLabel.pack()
    passwordEntry = tk.Entry(window)
    passwordEntry.pack()

    LButton = tk.Button(window, text="Login")
    LButton.pack()
    SButton = tk.Button(window, text="Sign Up")
    SButton.pack()


# def onClick():
#     connection = sqlite3.connect('Database/CentralisedDatabase.db')
#     cursor = connection.cursor()
#
#     cursor.execute('SELECT Password FROM LoginInformation WHERE Username = ?', ('Admin', ))
#     e = cursor.fetchall()
#
#     print(e)


def addComponents(window):
    LoginPage(window)
    onClick(window)


# userInput = int(input("""Welcome to St Mary's Logistic System:
#     What would you like to do?
#         [1] Add new Inventory
#         [2] Modify Inventory
#         [3] Track Shipments
#         [4] Generate Report
#         [5] Introduction To System.
#         [6] Quit
#             :: """))


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
    # setup_database()
    # run()
    onClick()
    # match userInput:
    #     case 1:
    #         print("You have selected option 1")
    #         try:
    #             valueStrip = []
    #             selectTable = str(input("What table do you want to add?"))
    #             tableColumns = str(input(f"""Enter in this format: {displayAllColumns(selectTable)}
    #                 :: """))
    #             # Take the User Input and Split it accordingly to be used for the  table placeholders
    #             splitColumns = tableColumns.split(",")
    #
    #             # Do a ForLoop to strip any WhiteSpace in the User Answer
    #             for value in splitColumns:
    #                 valueStrip.append(value.strip())
    #
    #             # Arguments: {Table}, {Placeholder Answers}.
    #             addToInventory(selectTable, valueStrip)
    #         except Exception as e:
    #             print(f"Something went wrong: {e}")
    #     case 2:
    #         print("You have selected option 2")
    #         try:
    #             valueStrip = []
    #             selectTable = str(input("What table do you want to Modify?"))
    #             tableColumns = str(input(f"""Enter in this format: {displayAllColumnsModify(selectTable)}
    #                     :: """))
    #             # Take the User Input and Split it accordingly to be used for the  table placeholders
    #             splitColumns = tableColumns.split(",")
    #
    #             # Do a ForLoop to strip any WhiteSpace in the User Answer
    #             for value in splitColumns:
    #                 valueStrip.append(value.strip())
    #
    #             # Arguments: {Table}, {Placeholder Answers}, {ID to modify}.
    #             modifyAllInventory(selectTable, valueStrip, 42)
    #         except Exception as e:
    #             print(f"Something went wrong: {e}")
    #     case 3:
    #         print("You have selected option 3")
    #     case 4:
    #         print("You have selected option 4")
    #     case 5:
    #         print("You have selected option 5")
    #     case 6:
    #         print("You have selected option 6")
    #     case 7:
    #         setup_database()
    #     case _:
    #         print("Invalid option")

# 4000, "Google", 400, "London", 123
# 1,'updated',213,'asd',123
# 1,Updated,123,asd,123
