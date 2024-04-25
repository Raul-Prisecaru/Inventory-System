import sqlite3
import tkinter as tk
from tkinter import ttk
# from AddNewInventory import *
# from AddNewInventory import *
from Features.AddNewInventory import *
# from Pages.MainMenuPages import getAllTables
import os
# Get the directory of the current script file
current_directory = os.path.dirname(__file__)
# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

components = {}
options = []
def getAllTables():
    tableinfo = []
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        tableinfo.append(table[1])
    tableinfo.remove("sqlite_sequence")
    tableinfo.remove("LoginInformation")
    # print(tableinfo)

    return tableinfo


def run():
    window = MainWindowConfig()
    addComponents(window)
    window.mainloop()


def MainWindowConfig():
    window = tk.Tk()
    window.geometry('600x500')
    window.title("Add Inventory SUStem")
    return window


def LoginPage(window):
    global tableOptions2
    tableLabel = tk.Label(window, text='Which Table would you like to deal with?')
    tableLabel.pack()
    tableSelect = tk.Entry(window)
    tableSelect.pack()

    columns = getAllColumns('Inventory')

    for column in columns:

        columnLabel = tk.Label(window, text=f'{column}')
        columnLabel.pack()

        columnEntry = tk.Entry(window)
        columnEntry.pack()

        components[column] = columnEntry

    addInventoryButton = tk.Button(window, text='Add To Inventory')
    addInventoryButton.pack()
    addInventoryButton.bind('<ButtonRelease-1>', onAddInventoryPress)

    # Dropdown Table code
    functionTableOption = getAllTables()
    for table in functionTableOption:
        options.append(table)

    tableOptions2 = ttk.Combobox(window, value=options)
    tableOptions2.pack()

    tableOptions2.bind('<<ComboboxSelected>>', onOptionSelected)

    return components

def onOptionSelected(event):
    global tableOptions2
    selectedTable = tableOptions2.get()
    print(f"{selectedTable} was selected")

    return selectedTable


def onAddInventoryPress(event):
    userValues = [entry.get() for entry in components.values()]
    addToInventory('Inventory', userValues)

    print(userValues)
    # components[column] = columnEntry
    # print(columnEntry)


def InventoryOptions(event):
    pass


def onSignUpButtonPress(event):
    pass


def addComponents(window):
    LoginPage(window)


getAllTables()
