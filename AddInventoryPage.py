import tkinter as tk
from AddNewInventory import *
components = {}


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
    rows = getAllColumns('Inventory')
    for row in rows:
        rowLabel = tk.Label(window, text=f'{row}')
        rowLabel.pack()

        columnEntry = tk.Entry(window)
        columnEntry.pack()
        print(rowLabel)




def InventoryOptions(event):
    pass


def onSignUpButtonPress(event):
    pass


def addComponents(window):
    LoginPage(window)

run()