import logging
import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)
# Construct the path to the database file relative to the current directory
log_path = os.path.join(current_directory, '..', 'logs', 'app.log')
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename=log_path, level=logging.INFO)
# logging.basicConfig(filename=log_path, level=logging.INFO)


def addToLogs(message):
    logging.info(message)


def displayLogs():
    with open(log_path, 'r') as logFile:
        for log in logFile:
            print(log.strip())
