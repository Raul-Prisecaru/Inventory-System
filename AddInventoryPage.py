import tkinter as tk
from AddNewInventory import *

components = {}
forloopvalue = []


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
    columns = getAllColumns('Inventory')
    for column in columns:

        columnLabel = tk.Label(window, text=f'{column}')
        columnLabel.pack()

        columnEntry = tk.Entry(window)
        columnEntry.pack()

        forloopvalue.append(columnEntry)

    addInventoryButton = tk.Button(window, text='Add To Inventory')
    addInventoryButton.pack()
    addInventoryButton.bind('<ButtonRelease-1>', onAddInventoryPress)

    return components


def onAddInventoryPress(event):
    value = forloopvalue

    print(value)
    # components[column] = columnEntry
    # print(columnEntry)


def InventoryOptions(event):
    pass


def onSignUpButtonPress(event):
    pass


def addComponents(window):
    LoginPage(window)


run()
