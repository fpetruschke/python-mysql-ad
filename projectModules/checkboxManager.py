import projectModules.executeSql as executeSql


def checkBoxStatus(oneIfOnlyAD, tablename, username, userfirstname, userpassword, userclass):
    # oneIfOnlyAD = True : new user will only inserted into AD
    # oneIfOnlyAD = False : new user will inserted into mysql AND AD

    if(oneIfOnlyAD == False):
        executeSql.executeMysqlInsert(tablename, username, userfirstname, userpassword, userclass)
        # @toDo: Skript for inserting into MySql AND AD !!!
    else:
        # @toDo: Create script for inserting user into MYSQL and then trigger another script from mysql to add into AD
        print('call of script for only creating user into active directory')


