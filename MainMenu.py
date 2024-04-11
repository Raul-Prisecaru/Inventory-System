import sqlite3
import tkinter as tk

def run():
    window = create_window()
    add_componenets(window)
    window.mainloop()
def create_window():
    window = tk.Tk()
    window.geometry("600x500")
    window.title("St Mary's Logistic System")
    return window

def add_componenets(window):
    textTotalRecords(window)

def textTotalRecords(window):
    Records_label = tk.Label(window)
    Records_label.config(text="Test", bg="#ddf", font=("Arial", 12))
    Records_label.grid(row=0, column=0, columnspan=2, sticky="EW")


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
    run()