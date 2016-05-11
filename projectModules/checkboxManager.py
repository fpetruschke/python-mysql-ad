import projectModules.executeSql as executeSql
import projectModules.adPython as adP
import config.adConfig as adC

def checkBoxStatus(oneIfOnlyAD, tablename, username, userfirstname, userpassword, userclass):
    adobj = adP.AdPython(adC.server,adC.username,adC.password)

    mergeduser = str(userclass[:3]) + "-" + str(username[:4]) + str(userfirstname[:2])
    # oneIfOnlyAD = True : new user will only inserted into AD
    # oneIfOnlyAD = False : new user will inserted into mysql AND AD

    if(oneIfOnlyAD == False):
        #(`user_id`, `name`, `firstname`, `username`, `password`, `class`)
        rows = executeSql.executeMysqlShowWhere('*',tablename,tablename+'.username = "' +mergeduser+'"' )
        if(len(rows)==0):
            executeSql.executeMysqlInsert(tablename, username, userfirstname, userpassword, userclass)
            adobj.syncsql([('0', username, userfirstname, mergeduser, userpassword, userclass)])
        else:
            print('User schon vorhanden')
    else:
        adobj.syncsql([('0', username, userfirstname, mergeduser, userpassword, userclass)])




