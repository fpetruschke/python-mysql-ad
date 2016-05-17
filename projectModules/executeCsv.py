# importing the csv module
import csv
# importing the module for executing sql statements
from projectModules import executeSql
# importing the filedialog module from tkinter for choosing a directory/file
from tkinter import filedialog
# importing the active directory configuration
import config.adConfig as adC
# importing the active directory module for executing belonging processes
import projectModules.adPython as adP

# function for importing data from csv-file to mysql db
def importFromCsv():
    """
    importFromCsv

    Opens a file chooser dialog and read the given csv line by line.
    Executes a full import into MySQL master and active directory.

    :return: does not return a value
    """
    adobj = adP.AdPython(adC.server, adC.username, adC.password)
    # get users choice for selecting a csv file
    filepathstring = filedialog.askopenfilename()
    f = open(filepathstring, 'r') # opens the csv file
    try:
        reader = csv.reader(f)  # creates the reader object
        # get the number of lines
        counter = 0
        for row in reader:      # iterates the rows of the file in orders
            # ignore the firstline which contains the header row
            if(counter != 0):
                rowDir = {
                    'name' : row[0],
                    'firstname': row[1],
                    'password': row[2],
                    'class': row[3]
                }
                mergeduser = str(row[3][:3]) + "-" + str(row[0][:4]) + str(row[1][:2])
                executeSql.executeMysqlInsert('user', rowDir['name'], rowDir['firstname'], rowDir['password'], rowDir['class'])
                adobj.syncsql([('0', rowDir['name'], rowDir['firstname'], mergeduser, rowDir['password'], rowDir['class'])], False)

            counter += 1
    finally:
        f.close()               # closing file reader


def importToAD():
    """
    importToAd

    This method will open a file chooser dialog and read the given csv line by line.
    It will execute a "AD-only" import.

    :return: no return value
    """
    adobj = adP.AdPython(adC.server, adC.username, adC.password)
    # get users choice for selecting a csv file
    filepathstring = filedialog.askopenfilename()
    f = open(filepathstring, 'r') # opens the csv file
    try:
        reader = csv.reader(f)  # creates the reader object
        # get the number of lines
        counter = 0
        for row in reader:      # iterates the rows of the file in orders
            # ignore the firstline which contains the header row
            if(counter != 0):
                rowDir = {
                    'name' : row[0],
                    'firstname': row[1],
                    'password': row[2],
                    'class': row[3]
                }
                mergeduser = str(row[3][:3]) + "-" + str(row[0][:4]) + str(row[1][:2])
                adobj.syncsql([('0', rowDir['name'], rowDir['firstname'], mergeduser, rowDir['password'], rowDir['class'])], False)
            counter += 1
    finally:
        f.close()               # closing file reader


def exportToCsv():
    """
    exportToCsv

    Will open a directory chooser dialog for exporting the MySQL master table data to.

    :return: no return value but .csv-file creation
    """
    path = filedialog.asksaveasfilename()
    rows = executeSql.executeMysqlShow('*', 'user')
    headrow = ['Nutzer-Id', 'Name', 'Vorname', 'Nutzername', 'Password', 'Klasse']
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(headrow)
        for row in rows:
            writer.writerow(row)