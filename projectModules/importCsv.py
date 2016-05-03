import csv      # imports the csv module
from tkinter import filedialog

"""
###################################################################################
TEST FOR IMPORTING DATA FROM CSV
###################################################################################

"""

#tk.withdraw() # we don't want a full GUI, so keep the root window from appearing
filepathstring = filedialog.askopenfilename()

f = open(filepathstring, 'r') # opens the csv file
try:
    reader = csv.reader(f)  # creates the reader object
    for row in reader:      # iterates the rows of the file in orders
        print(row)          # prints each row
finally:
    f.close()               # closing file reader