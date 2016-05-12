import unittest

import os.path
import pages.aboutPage as about

"""
TestsPagesAllPagesExistent
Checks if all pages are existent
"""
# @toDo: Add tests for all pages
class TestsPagesAllPagesExistent(unittest.TestCase):

    def openAbout(self):
        return os.path.isfile(about.__file__)

    def testabout(self):
        self.assertTrue(self.openAbout())


def main():
    unittest.main()

if __name__ == '__main__':
    main()