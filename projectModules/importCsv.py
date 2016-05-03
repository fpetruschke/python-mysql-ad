import csv      # imports the csv module
from projectModules import executeSql
from tkinter import filedialog

"""
###################################################################################
TEST FOR IMPORTING DATA FROM CSV
###################################################################################

"""

def importFromCsv():
    #tk.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filepathstring = filedialog.askopenfilename()

    f = open(filepathstring, 'r') # opens the csv file
    try:
        reader = csv.reader(f)  # creates the reader object
        for row in reader:      # iterates the rows of the file in orders
            rowDir = {
                'name' : row[0],
                'firstname': row[1],
                'password': row[2],
                'class': row[3]
            }
            executeSql.executeMysqlInsert('user', rowDir)
    finally:
        f.close()               # closing file reader