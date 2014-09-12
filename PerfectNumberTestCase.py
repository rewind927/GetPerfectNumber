import unittest
from PerfectNumber import *

class PerfectNumberTestCase(unittest.TestCase):
    def test_is_perfect_number1(self):
        self.assertEquals(isPerfectNumber(6),True)

    def test_is_perfect_number2(self):
        self.assertEquals(isPerfectNumber(28),True)

    def test_is_perfect_number3(self):
        self.assertEquals(isPerfectNumber(496),True)

    def test_is_perfect_number4(self):
        self.assertEquals(isPerfectNumber(8128),True)

    def test_is_perfect_number5(self):
        self.assertEquals(isPerfectNumber(33550336),True)

    def test_is_perfect_number6(self):
        self.assertEquals(isPerfectNumber(33550338),False)

    def test_is_perfect_number7(self):
        self.assertEquals(isPerfectNumber(1000),False)

    def test_is_perfect_number8(self):
        self.assertEquals(isPerfectNumber(100),False)

    def test_is_perfect_number9(self):
        self.assertEquals(isPerfectNumber(10),False)

if __name__ == '__main__':
    unittest.main()
