import sqlite3
import tkinter as tk
from tkinter import ttk
from Pages.AddInventoryPage import run as AddInventoryPageRun
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
txt_path = os.path.join(current_directory, '..', 'Pages', 'MainMenuOptions.txt')
print(txt_path)

components = {}
options = []
selectedTable = {}


# forloopvalue = []

def getAllTables():
    tableList = []
    with open(txt_path, 'r') as Options:
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
    global tableOptions2
    tables = getAllTables()
    userLabel = tk.Label(window, text="Welcome user")
    userLabel.pack()

    for index, table in enumerate(tables):
        tableButton = tk.Button(window, text=f'{table}')
        tableButton.pack()
        tableButton.bind('<ButtonRelease-1>', lambda event, index=index: onAddInventoryPress(event, index))



    return


def onAddInventoryPress(event, index):
    if index == 0:
        AddInventoryPageRun()
    elif index == 1:
        print("Index 1 pressed")
    elif index == 2:
        print("Index 2 pressed")
    elif index == 3:
        print("Index 3 pressed")


def addComponents(window):
    LoginPage(window)

# getAllTables()
# run()
