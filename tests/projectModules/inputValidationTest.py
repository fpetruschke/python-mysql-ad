import unittest

import projectModules.inputValidation as inputValidation

"""
TestsProjectModulesInputValidation
Tests if the validator module works properly
"""
class TestsProjectModulesInputValidation(unittest.TestCase):

    def getValidPwd(self):
        return 'ValidPwd1'

    def getInvalidPwd(self):
        return '123'

    def getEmptyInput(self):
        return ''

    def testValidPassword(self):
        self.assertTrue(inputValidation.validatePassword(self.getValidPwd()))

    def testInvalidPassword(self):
        self.assertFalse(inputValidation.validatePassword(self.getInvalidPwd()))

    def testEmptyInput(self):
        self.assertFalse(inputValidation.validateIfEmpty(self.getEmptyInput()))

def main():
    unittest.main()

if __name__ == '__main__':
    main()