import sqlite3;
import tkinter as tk
# from AddNewInventory import *
# from AddNewInventory import *
# from Features.AddNewInventory import *


components = {}
# forloopvalue = []

def getAllTables():
    tableList = []
    with open ('Pages/MainMenuOptions.txt', 'r') as Options:
        for option in Options:
             tableList.append(option)

    print(tableList)
    return tableList


def run():
    window = MainWindowConfig()
    addComponents(window)
    window.mainloop()


def MainWindowConfig():
    window = tk.Tk()
    window.geometry('600x500')
    window.title("Main Menu")
    return window


def LoginPage(window):
    tables = getAllTables()
    userLabel = tk.Label(window, text="Welcome user")
    userLabel.pack()

    for index, table in enumerate(tables):
        tableButton = tk.Button(window, text=f'{table}')
        tableButton.pack()
        components[table] = tableButton
        tableButton.bind('<ButtonRelease-1>', lambda event, index=index: onAddInventoryPress(event, index))
    return


def onAddInventoryPress(event, index):
    if index == 0:
           print("Index 0 pressed")
    elif index == 1:
            # Open the second file
            print("Index 1 pressed")



def addComponents(window):
    LoginPage(window)


# getAllTables()
run()