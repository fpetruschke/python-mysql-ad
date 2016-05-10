import re

def validatePassword(pwd):
    # ([A-Z])\w{7,}[0-9]+
    # OLD: ([a-z]*|[A-Z]*|[0-9]*|.{7,34})
    if re.match("^([A-Z])\w{7,}[0-9]+$", pwd):
        return True
    else:
        return False

def validateIfEmpty(input):
    if input == "":
        return False
    else:
        return True