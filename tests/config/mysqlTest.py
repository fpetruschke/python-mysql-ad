import unittest

import os.path
import config.mysqlConfig as mysqlConfig

"""
TestsConfigMysqlConfig
Checks if MysqlConfig.py is existent
"""
class TestsConfigMysqlConfig(unittest.TestCase):

    def openMySqlConfig(self):
        return os.path.isfile(mysqlConfig.__file__)

    def testLoadMysqlConfig(self):
        fileIsExistent = self.openMySqlConfig()
        self.assertTrue(fileIsExistent)


def main():
    unittest.main()

if __name__ == '__main__':
    main()