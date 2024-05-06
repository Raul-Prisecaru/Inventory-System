import os

# Get the directory of the current script file
current_directory = os.path.dirname(__file__)

# Construct the path to the database file relative to the current directory
TOSFile = os.path.join(current_directory, '..', 'TextFile', 'TermsService.txt')


def displayService():
    with open(TOSFile, 'r') as File:
        for line in File:
            print(line, end='')


def termsService(userSelection):
    if userSelection == 1:
        return True
    else:
        return False
