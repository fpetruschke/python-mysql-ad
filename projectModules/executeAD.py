import projectModules.executeSql as executeSql
import config.adConfig as adConf
import wmi

# preparing ssh connection to active directory
def executeCommandOnShellViaSsh(command):
    c=wmi.WMI(adConf.server,user=adConf.username,password=adConf.password)
    process_id, return_value = c.Win32_Process.Create(CommandLine=command)

# insert new user using the preconfigured ssh connection
def insertNewUser(nameOfNewUser, PhoneNumberOfNewUser):
    executeCommandOnShellViaSsh("powershell.exe /c "
                                "Set-ADUser " + nameOfNewUser +
                                " -OfficePhone " + PhoneNumberOfNewUser)


# execute insertion of new user with phone number
insertNewUser('Ferdi1000', "1234")


# module for inserting data into AD
#def insertUserIntoAD(userId):
#    userData = executeSql.executeMysqlShowWhere('*','user','user_id='+ str(userId))
#    if (0 == userData):
#        print('No user with id ' + userId + ' found.')
#    else:
#        print(userData)

#insertUserIntoAD(26)