import sqlite3
import tkinter as tk
from tkinter import ttk
from Features.AddNewInventory import *
# from Pages.MainMenuPages import getAllTables
import os
# Get the directory of the current script file
current_directory = os.path.dirname(__file__)
# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

components = {}
options = []

userOption = ''
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
    global userOption

    def display_components():
        global userOption
        columns = getAllColumns(tableOptions2.get())
        userOption = tableOptions2.get()
        print(f'tableOptions2: {tableOptions2.get()}')
        for column in columns:
            columnLabel = tk.Label(window, text=f'{column}')
            columnLabel.pack()

            columnEntry = tk.Entry(window)
            columnEntry.pack()

            components[column] = columnEntry

        addInventoryButton = tk.Button(window, text='Add to table')
        addInventoryButton.pack()
        addInventoryButton.bind('<ButtonRelease-1>', onAddInventoryPress)

    tableLabel = tk.Label(window, text='Which Table would you like to deal with?')
    tableLabel.pack()

    # Create the dropdown table options
    functionTableOption = getAllTables()
    print(f'functionTableOption: {functionTableOption}')
    if not functionTableOption:
        print('No options available. Please select an option.')
        return  # Exit the function if there are no options

    tableOptions2 = ttk.Combobox(window, value=functionTableOption)
    tableOptions2.pack()

    # Define the function to be executed when an option is selected
    def on_option_selected(event):
        display_components()

    # Bind the function to the ComboboxSelected event
    tableOptions2.bind('<<ComboboxSelected>>', on_option_selected)

    return components


# def onOptionSelected(event):
#     global tableOptions2
#     selectedTable = tableOptions2.get()
#     print(f"{selectedTable} was selected")
#
#     return selectedTable


def onAddInventoryPress(event):
    userValues = [entry.get() for entry in components.values()]
    print(f'components: {components}')
    print(f'userValues: {userValues}')
    print(f'userOption: {userOption}')
    addToInventory(userOption, userValues)

    # components[column] = columnEntry
    # print(columnEntry)


def InventoryOptions(event):
    pass


def onSignUpButtonPress(event):
    pass


def addComponents(window):
    LoginPage(window)


getAllTables()
