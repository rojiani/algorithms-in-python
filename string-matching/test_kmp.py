import unittest
from kmp import *

class TestKMP(unittest.TestCase):
    """Tests for 'kmp.py'."""

    def setUp(self):
        self.P1 = 'aaax'
        self.P2 = 'ababaca'
        self.P3 = 'aaaxa'
        self.P4 = 'aaaxaa'
        self.P5 = 'aaaxaaa'

        self.P6 = 'abac'
        self.T1 = 'abac'
        self.T2 = 'xabacabac'
        self.T3 = 'abacabacabac'
        self.T4 = 'xxxxxxxxabac'

    def tearDown(self):
        pass

    def testComputePrefixFunction(self):
        self.assertEqual(compute_prefix_function(self.P1), [0, 1, 2, 0])
        self.assertEqual(compute_prefix_function(self.P2), [0, 0, 1, 2, 3, 0, 1])
        self.assertEqual(compute_prefix_function(self.P3), [0, 1, 2, 0, 1])
        self.assertEqual(compute_prefix_function(self.P4), [0, 1, 2, 0, 1, 2])
        self.assertEqual(compute_prefix_function(self.P5), [0, 1, 2, 0, 1, 2, 3])

    def testComputePrefixFunctionHwProblem(self):
        pattern = 'ababbabbabbababbabb';
        expected = [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(compute_prefix_function(pattern), expected)

    def testKmpMatcher(self):
        self.assertEqual(kmp_matcher(self.T1, self.P6), [0])
        self.assertEqual(kmp_matcher(self.T2, self.P6), [1, 5])
        self.assertEqual(kmp_matcher(self.T3, self.P6), [0, 4, 8])
        self.assertEqual(kmp_matcher(self.T4, self.P6), [8])

if __name__=='__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise