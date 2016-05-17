# importing module for executing sql statements
import projectModules.executeSql as executeSql
# importing activeDirectory module for executing belonging processes
import projectModules.adPython as adP
# importing active directory configuration
import config.adConfig as adC


def checkBoxStatus(oneIfOnlyAD, tablename, username, userfirstname, userpassword, userclass):
    """
    checkBoxStatus

    Is responsible for processing the "only insert into AD" action

    :param oneIfOnlyAD: True or False - checkbox status
    :param tablename: name of the MySQL master table
    :param username: name of the user to insert
    :param userfirstname: firstname of the user to insert
    :param userpassword: password for the new user
    :param userclass: class for the new inserted user
    :return: does only print "user already exists" in that case; else calls other functions
    """
    adobj = adP.AdPython(adC.server,adC.username,adC.password)

    mergeduser = str(userclass[:3]) + "-" + str(username[:4]) + str(userfirstname[:2])
    # oneIfOnlyAD = True : new user will only inserted into AD
    # oneIfOnlyAD = False : new user will inserted into mysql AND AD

    if(oneIfOnlyAD == False):
        #(`user_id`, `name`, `firstname`, `username`, `password`, `class`)
        rows = executeSql.executeMysqlShowWhere('*',tablename,tablename+'.username = "' +mergeduser+'"' )
        if(len(rows)==0):
            executeSql.executeMysqlInsert(tablename, username, userfirstname, userpassword, userclass)
            adobj.syncsql([('0', username, userfirstname, mergeduser, userpassword, userclass)],False)
        else:
            print('user already exists.')
    else:
        adobj.syncsql([('0', username, userfirstname, mergeduser, userpassword, userclass)])
