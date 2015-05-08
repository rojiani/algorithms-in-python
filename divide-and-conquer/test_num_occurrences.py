import unittest
from num_occurrences import *

class TestNumOccurrences(unittest.TestCase):
    """Tests for 'mergesort.py'."""

    def setUp(self):
        self.A = []
        self.B = [5]
        self.C = [5, 10, 15]
        self.D = [-2, 2, 2, 2, 4, 7]
        self.E = [1, 1, 1, 1, 4, 5, 7, 7, 9]
        self.F = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 9, 10]

    def tearDown(self):
        pass

    def testNumX(self):
        self.assertEqual(0, count_x(self.A, 8))
        self.assertEqual(1, count_x(self.B, 5))
        self.assertEqual(1, count_x(self.C, 5))
        self.assertEqual(3, count_x(self.D, 2))
        self.assertEqual(4, count_x(self.E, 1))
        self.assertEqual(1, count_x(self.E, 5))
        self.assertEqual(2, count_x(self.E, 7))
        self.assertEqual(10, count_x(self.F, 1))


if __name__=='__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise