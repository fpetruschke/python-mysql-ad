import unittest

import config.style as style

"""
TestsConfigStyle
Tests if the styles can be loaded and contain expected values
"""
class TestsConfigStyle(unittest.TestCase):

    def getLargeFontBold(self):
        return style.LARGE_FONT_BOLD

    def testLargeFontBold(self):
        self.assertEqual(self.getLargeFontBold(), ('Helvetica', 12, 'bold'))

    def getSmallFont(self):
        return style.SMALL_FONT

    def testSmallFont(self):
        self.assertEqual(self.getSmallFont(), ('Helvetica', 8))

    def getMargin10(self):
        return style.MARGIN10

    def testMargin10(self):
        self.assertEqual(self.getMargin10(), {'pady': 10, 'padx': 10})

def main():
    unittest.main()

if __name__ == '__main__':
    main()