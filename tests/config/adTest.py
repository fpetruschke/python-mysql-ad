import unittest

import os.path
import config.adConfig as adConfig

"""
TestsConfigMysqlConfig
Checks if AdConfig.py is existent
"""
class TestsConfigMysqlConfig(unittest.TestCase):

    def openAdConfig(self):
        return os.path.isfile(adConfig.__file__)

    def testLoadAdConfig(self):
        fileIsExistent = self.openAdConfig()
        self.assertTrue(fileIsExistent)


def main():
    unittest.main()

if __name__ == '__main__':
    main()