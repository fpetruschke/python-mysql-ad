import projectModules.executeSql as executeSql
import config.adConfig as adConf
import wmi

def executeCommandOnShellViaSsh(command):
    c=wmi.WMI(adConf.server,user=adConf.username,password=adConf.password)
    process_id, return_value = c.Win32_Process.Create(CommandLine=command)

# module for inserting data into AD
#def insertUserIntoAD(userId):
#    userData = executeSql.executeMysqlShowWhere('*','user','user_id='+ str(userId))
#    if (0 == userData):
#        print('No user with id ' + userId + ' found.')
#    else:
#        print(userData)

#insertUserIntoAD(26)


executeCommandOnShellViaSsh("powershell.exe /c Set-ADUser Ferdi1 -OfficePhone 1234")

