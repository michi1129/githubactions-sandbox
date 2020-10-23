import calc
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 4), 1)

    def test_add2(self):
        self.assertEqual(calc.add2(7), 9)
