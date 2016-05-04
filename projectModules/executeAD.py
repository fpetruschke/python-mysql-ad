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

#Add user account in local server computer
def addNewUser(username, password, fullname):
    #net user username password /add /fullname:"name"
    executeCommandOnShellViaSsh()

#Delete user account in local server computer
def deleteUser(localgroup, groupname):
    # net localgroup groupname /delete
    executeCommandOnShellViaSsh()

#Add user account to a local group
def addUserAccountToGroup(localgroup, groupname, username):
    #net localgroup groupname username /add
    executeCommandOnShellViaSsh()

#Remove user account to a local group
def deleteUsernameFromGroup(localgroup, group, username):
    #net localgroup groupname username /delete
    executeCommandOnShellViaSsh()


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