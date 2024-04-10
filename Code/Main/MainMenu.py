import _sqlite3
LogisticSystemOption = int(input("""Welcome to St Mary's Logistic System
What would you like to do?
[1] - Add New Inventory
[2] - Manage Inventory
[3] - Track All Shipment
[4] - Generate Reports for Inventory Status
:: """))

def setup_database():
    pass

while True:
    match LogisticSystemOption:
        case 1:
            print("You have selected 1")

        case 2:
            print("You have selected 2")

        case 3:
            print("You have selected 3")

        case 4:
            print("You have selected 4")

        case _:
            print("Invalid Option was selected")


if __name__ == '__main__':
    pass