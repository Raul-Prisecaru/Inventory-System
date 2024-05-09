import sqlite3
import os
import timeit

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
database_path = os.path.join(current_directory, '..', 'Database', 'CentralisedDatabase.db')


# Create connection to the database
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# Function to execute the query without an index
def query_without_index():
    cursor.execute("SELECT * FROM Inventory WHERE InventoryPrice > 50")
    rows = cursor.fetchall()

# Function to execute the query with an index
def query_with_index():
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_InventoryPrice ON Inventory (InventoryPrice)")
    cursor.execute("SELECT * FROM Inventory WHERE InventoryPrice > 50")
    rows = cursor.fetchall()

# Measure the execution time without an index
time_without_index = timeit.timeit(query_without_index, number=10000)

# Measure the execution time with an index
time_with_index = timeit.timeit(query_with_index, number=10000)

# Print the results
print(f"Time taken without index: {time_without_index} seconds")
print(f"Time taken with index: {time_with_index} seconds")

# Close the connection
connection.close()