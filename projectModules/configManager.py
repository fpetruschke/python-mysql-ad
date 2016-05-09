# get config for settings
import config.adConfig as adConf
import config.mysqlConfig as mysqlConf

# setConfig(<dictionary>)
#
# turns the values in the config files into the given values.
# If writeToFile is True, not only temp values will be set but configs overwritten
# adConfig:     'adHost', 'adUser', 'adPwd'
# mysqlConfig:  'mysqlHost', 'mysqlDb', 'mysqlUser', 'mysqlPwd'
def setConfig(configureDict):
    dict = configureDict
    if(False==dict['writeToFile']):
        # setting ad config
        adConf.server   = dict['adHost']
        adConf.username = dict['adUser']
        adConf.password = dict['adPwd']
        # setting mysql config
        mysqlConf.hostName  = dict['mysqlHost']
        mysqlConf.dbName    = dict['mysqlDb']
        mysqlConf.dbUser    = dict['mysqlUser']
        mysqlConf.dbPassword= dict['mysqlPwd']
    else:
        overrideMysqlConfigFile(dict)
        overrideAdConfigFile(dict)

def overrideMysqlConfigFile(dict):
    # open file, truncate its content and write new config
    target = open("config/mysqlConfig.py", 'w')
    target.truncate()
    target.write("hostName = '" + dict['mysqlHost'] + "'")
    target.write("\n")
    target.write("dbName = '" + dict['mysqlDb'] + "'")
    target.write("\n")
    target.write("dbUser = '" + dict['mysqlUser'] + "'")
    target.write("\n")
    target.write("dbPassword = '" + dict['mysqlPwd'] + "'")
    target.write("\n")
    target.close()

def overrideAdConfigFile(dict):
    # open file, truncate its content and write new config
    target = open("config/adConfig.py", 'w')
    target.truncate()
    target.write("server = '" + dict['adHost'] + "'")
    target.write("\n")
    target.write("username = '" + dict['adUser'] + "'")
    target.write("\n")
    target.write("password = '" + dict['adPwd'] + "'")
    target.write("\n")
    target.close()