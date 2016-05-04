import projectModules.executeSql as executeSql

def checkBoxStatus(oneIfOnlyAD, tablename, username, userfirstname, userpassword, userclass):
    # oneIfOnlyAD = 1 : new user will only inserted into AD
    # oneIfOnlyAD = 0 : new user will inserted into mysql AND AD
    if(0 == oneIfOnlyAD):
        executeSql.executeMysqlInsert(tablename, {'name': username, 'firstname': userfirstname,
                                           'password': userpassword, 'class': userclass})
    else:
        # @toDo: Create script for inserting user into MYSQL and then trigger another script from mysql to add into AD
        print('call of script for only creating user into active directory')


