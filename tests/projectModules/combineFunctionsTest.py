import unittest

import projectModules.combineFunctions as combine

"""
TestsProjectModulesCombineFunctions
Tests if the combine_funcs can handle more than one function.
Combine_funcs came up since tkinter button can only handle one command by default.
"""
class TestsProjectModulesCombineFunctions(unittest.TestCase):
    def function1(self):
        x = 10
        return x

    def function2(self):
        y = 20
        return y

    def test(self):
        result = combine.combine_funcs(self.function1(), self.function2())
        self.assertTrue(self, result)

def main():
    unittest.main()

if __name__ == '__main__':
    main()