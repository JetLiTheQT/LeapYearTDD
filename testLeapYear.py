import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):
    def testFour(self):
        self.assertEqual(LeapYear.leap(2004), "Leap Year")
    def testExceptHundred(self):
        self.assertEqual(LeapYear.leap(2100), "Not Leap Year")