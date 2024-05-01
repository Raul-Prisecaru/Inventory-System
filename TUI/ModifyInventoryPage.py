import sqlite3
import tkinter as tk
from tkinter import ttk

from Features.AddNewInventory import getAllColumns
from Features.ModifyInventory import *
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')

# Used to store user response to add to the DB
components = {}


# Function to get all of the tables found in the DB
def getAllTables():
    # List to store all of the tables
    tableinfo = []

    # Connect to Database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Execute Query where the type is table and get all of the results with fetchall()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Store the results in the table
    for table in tables:
        tableinfo.append(table[1])
    # Remove the irrelevant tables
    tableinfo.remove("sqlite_sequence")
    tableinfo.remove("LoginInformation")

    # Return List to display the tables to the user later on
    return tableinfo


# Function to run the Window
def run():
    window = MainWindowConfig()
    addComponents(window)
    window.mainloop()


# Function to Configure Window
def MainWindowConfig():
    window = tk.Tk()
    window.geometry('600x500')
    window.title("Modify Inventory System")
    return window


# Function to create options for user to interact with DB
def DBInteract(window):
    # Responsible for managing options shown in Combobox
    global tableOptionComboBox

    # Create label to inform user what dropbox is responsible for
    tableLabel = tk.Label(window, text='Which Table would you like to deal with?')
    tableLabel.pack()

    # Get all the tables available from getAllTables() and print for debugging purposes.
    functionTableOption = getAllTables()
    print(f'functionTableOption: {functionTableOption}')

    # Create Dropbox containing all the tables stored in 'functionTableOption'
    tableOptionComboBox = ttk.Combobox(window, value=functionTableOption)
    tableOptionComboBox.pack()

    # Bind the function to the ComboboxSelected event
    tableOptionComboBox.bind('<<ComboboxSelected>>', lambda event: displayComponents(window, event))


# Comment
def displayComponents(window, event):
    # Used getAllColumns(Table) function to get all of the columns available
    # tableOptionComboBox.get() to say what table to look for.
    columns = getAllColumns(tableOptionComboBox.get())

    # Print tableOptionComboBox.get() for debugging purposes
    print(f'tableOptionComboBox: {tableOptionComboBox.get()}')

    # Do forLoop to create Labels and Entry per column available in a table
    for column in columns:
        # Create Labels with Column Name
        columnLabel = tk.Label(window, text=f'{column}')
        columnLabel.pack()

        # Create Entry with Column Name
        columnEntry = tk.Entry(window)
        columnEntry.pack()
        components[column] = columnEntry

    # Create Button and upon left click '<ButtonRelease-1>', go to onAddInventoryPress Function
    addInventoryButton = tk.Button(window, text='Add to table')
    addInventoryButton.pack()
    addInventoryButton.bind('<ButtonRelease-1>', onAddInventoryPress)


# Comment
def onAddInventoryPress(event):
    # Get the user responses stored in the Entry
    userValues = [entry.get() for entry in components.values()]

    # Print for Debugging purposes
    print(f'components: {components}')
    print(f'userValues: {userValues}')
    print(f'userValues: {userValues[0]}')
    print(f'modifyAllInventory: {tableOptionComboBox.get()}')

    # addToInventory takes two arguments, Table and values for placeholders.
    # tableOptionComboBox.get() is used to define what table to put the values in
    # userValues contains the relevant number of values to be used in the placeholder found in SQLQuery

    userValuesNoID = userValues[1:]
    print(f'userValuesNoID: {userValuesNoID}')
    modifyAllInventory(tableOptionComboBox.get(), userValuesNoID, userValues[0])


# Defines what to run
def addComponents(window):
    DBInteract(window)