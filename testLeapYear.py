import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):
    def testFour(self):
        self.assertEqual(LeapYear.leap(2000), LeapYear)