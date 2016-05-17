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
    """
    setConfig

    Sets the given configuration as temporary configuration if dict['writeToFile'] is False -
    that will be deleted after restarting the program!
    If it's True, it will call the methods for overwriting the existing congiguration.
    Will be refreshed AFTER RESTARTING the program!

    :param configureDict: dictionary containing the new configuration
    :return: does not return a value but calls the mentioned functions
    """
    dict = configureDict
    if(False==dict['writeToFile']):
        # setting ad config
        adConf.server   = dict['adHost']
        adConf.username = dict['adUser']
        adConf.password = dict['adPwd']
        adConf.domain1 = dict['adDomain1']
        adConf.domain2 = dict['adDomain2']
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
    target.write("#needed for initial build of general OU structure")
    target.write("\n")
    target.write("domain1 = '" + dict['adDomain1'] + "'")
    target.write("\n")
    target.write("domain2 = '" + dict['adDomain2'] + "'")
    target.write("\n")
    target.write("dict = [domain2, domain1, 'Benutzer','Schueler','Klassen','IT']")
    target.close()