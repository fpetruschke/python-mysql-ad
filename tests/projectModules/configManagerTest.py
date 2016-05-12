import unittest

import projectModules.configManager as configManager
import config.adConfig as adConf
import config.mysqlConfig as mysqlConf

"""
TestsProjectModulesConfigManager
Tests if the configManager saves tmp configuration properly
"""
class TestsProjectModulesConfigManager(unittest.TestCase):

    def creatingDictionary(self):
        # setting a test dictionary with test settings
        dict = {
            'writeToFile': False,
            'adHost'    : 'testAdHost',
            'adUser'    : 'testAdUser',
            'adPwd'     : 'testAdPwd',
            'adDomain1' : 'testDomain1',
            'adDomain2' : 'testDomain2',
            'mysqlHost' : 'testMysqlHost',
            'mysqlDb'   : 'testMysqlDb',
            'mysqlUser' : 'testMysqlUser',
            'mysqlPwd'  : 'testMysqlPwd'
        }
        return dict

    def overwriteTmpConfigs(self):
        configManager.setConfig(self.creatingDictionary())

    def getTmpConfigs(self):
        configDict = {
            'writeToFile': False,
            'adHost'    : adConf.server,
            'adUser'    : adConf.username,
            'adPwd'     : adConf.password,
            'adDomain1' : adConf.domain1,
            'adDomain2' : adConf.domain2,
            'mysqlHost' : mysqlConf.hostName,
            'mysqlDb'   : mysqlConf.dbName,
            'mysqlUser' : mysqlConf.dbUser,
            'mysqlPwd'  : mysqlConf.dbPassword
        }
        return configDict

    def test(self):
        self.overwriteTmpConfigs()
        tmpDict = self.creatingDictionary()
        confDict = self.getTmpConfigs()
        self.assertEqual(tmpDict, confDict)

def main():
    unittest.main()

if __name__ == '__main__':
    main()