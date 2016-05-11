import re

# checks if given pwd matches the password policies for active directory
def validatePassword(pwd):
    if re.match("^([A-Z])\w{7,}[0-9]+$", pwd):
        return True
    else:
        return False

# checks if a given input is empty
def validateIfEmpty(input):
    if input == "":
        return False
    else:
        return True