import sqlite3
import tkinter as tk
from Features.Login import Login, SignUp
from TUI.AddInventoryTUI import run as AddInventoryPageRun
from TUI.MainMenuPages import run as MainMenuPageRun
components = {}


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
    components['loginEntry'] = loginEntry

    passwordLabel = tk.Label(window, text="Password: ")
    passwordLabel.pack()

    passwordEntry = tk.Entry(window)
    passwordEntry.pack()
    components['passwordEntry'] = passwordEntry

    LButton = tk.Button(window, text="Login")
    LButton.pack()
    LButton.bind("<ButtonRelease-1>", onLoginButtonPress)
    SButton = tk.Button(window, text="Sign Up")
    SButton.pack()
    SButton.bind("<ButtonRelease-1>", onSignUpButtonPress)


def onLoginButtonPress(event):
    Username = components['loginEntry'].get()
    Password = components['passwordEntry'].get()
    if Login(f'{Username}', f'{Password}'):
        MainMenuPageRun()
    else:
        print('Cannot switch page')


def onSignUpButtonPress(event):
    Username = components['loginEntry'].get()
    Password = components['passwordEntry'].get()
    SignUp(f'{Username}', f'{Password}')



def addComponents(window):
    LoginPage(window)

# def setup_database():
#     try:
#         connection = sqlite3.connect('Database/CentralisedDatabase.db')
#         cursor = connection.cursor()
#
#         with open('Database/CentralisedDatabase.sql', "r") as sql_file:
#             sql_script = sql_file.read()
#
#         cursor.executescript(sql_script)
#
#         connection.commit()
#         connection.close()
#         print("Database Successfully Created")
#
#     except NameError:
#         print("NameError Caught: Database (.db) Not Found.")
#     except Exception as e:
#         print("Error Caught: " + str(e))


if __name__ == '__main__':
    # setup_database()
    run()
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
