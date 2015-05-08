import unittest
from mergesort import *

class TestMergeSort(unittest.TestCase):
    """Tests for 'mergesort.py'."""

    def setUp(self):
        self.A = [5]
        self.B = [5, 10, 15]
        self.C = [-2, 10, 4]
        self.D = [-2, 5, 2, 1]
        self.E = [1, 4, 1, 2, 1, 7, 2, 1]
        self.F = ['a', 'c', 'z', 'x', 'm']
        self.G = ['abba', 'zabba', 'chimichanga', 'quality']

    def tearDown(self):
        pass

    def test_merge(self):
        self.assertEqual([1, 2, 3, 4, 5], merge([1, 4], [2, 3, 5]))
        self.assertEqual([1, 2, 3, 4, 5], merge([], [1, 2, 3, 4, 5]))
        self.assertEqual([1, 2, 3, 4, 5], merge([1, 2, 3, 4, 5], []))
        self.assertEqual([1, 2, 3, 4, 5], merge([1, 3, 4], [2, 5]))
        self.assertEqual(self.A, merge([5], []))

    def test_mergesort_simple(self):
        self.assertEqual([5], mergesort(self.A))
        self.assertEqual([5, 10, 15], mergesort(self.B))

    def test_mergesort_neg(self):
        self.assertEqual([-2, 4, 10], mergesort(self.C))
        self.assertEqual([-2, 1, 2, 5], mergesort(self.D))

    def test_mergesort_duplicates(self):
        self.assertEqual([1, 1, 1, 1, 2, 2, 4, 7], mergesort(self.E))

    def test_mergesort_strings(self):
        self.assertEqual(['a', 'c', 'm', 'x', 'z'], mergesort(self.F))
        self.assertEqual(['abba', 'chimichanga', 'quality', 'zabba'], mergesort(self.G))

if __name__=='__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise