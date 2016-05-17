# importing module re for checking regular expressions
import re

# checks if given pwd matches the password policies for active directory
def validatePassword(pwd):
    """
    validatePassword

    Method checks whether the given password matches the current password policies of teh active directory or not.

    :param pwd: password the user entered for creating a new user entry
    :return: True or False
    """
    if re.match("^([A-Za-z])\w{7,}[0-9]+$", pwd):
        return True
    else:
        return False


def validateIfEmpty(input):
    """
    validateIfEmpty

    Method for checking if the given input parameter is an empty string or not.

    :param input: input string
    :return: True or False
    """
    if input == "":
        return False
    else:
        return True