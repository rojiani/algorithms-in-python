import unittest
from inversions import *

class TestInversions(unittest.TestCase):
    """Tests for 'inversions.py'."""

    def setUp(self):
        self.A = [1, 3, 2, 4]                # (3,2)
        self.B = [1, 6, 3, 2, 4, 5, 7, 8]    # (6,2) (6,3) (6,4) (6,5) (3,2)
        self.C = [1, 3, 2, 4, 6, 5]          # (3,2) (6,5)

    def tearDown(self):
        pass

    def test_merge_and_count(self):
        inv = []
        merge_and_count([1], [2], inv)
        self.assertEqual([], inv)
        # self.assertEqual([], merge_and_count([1], [2], [])[1])

        inv = []
        merge_and_count([2], [1], inv)
        self.assertEqual(['(2,1)'], inv)

        # self.assertEqual(['(2,1)'], merge_and_count([2], [1], [])[1])

        inv = []
        merge_and_count([1, 3], [2], inv)
        self.assertEqual(['(3,2)'], inv)
        # self.assertEqual(['(3,2)'], merge_and_count([1, 3], [2], [])[1])

        inv = []
        merge_and_count([1, 3], [2, 4], inv)
        self.assertEqual(['(3,2)'], inv)
        # self.assertEqual(['(3,2)'], merge_and_count([1, 3], [2, 4], [])[1])

        inv = []
        merge_and_count([1, 3, 5], [2, 4, 6], inv)
        self.assertEqual(['(3,2)', '(5,4)'], inv)        
        # self.assertEqual(['(3,2)', '(5,4)'], merge_and_count([1, 3, 5], [2, 4, 6], [])[1])
        
        inv = []
        merge_and_count([4, 5], [1, 2, 3], inv)
        self.assertEqual(['(4,1)', '(4,2)', '(4,3)'], inv)    
        # self.assertEqual(['(4,1)', '(4,2)', '(4,3)'], merge_and_count([4, 5], [1, 2, 3], [])[1])


    def test_inversions(self):
        self.assertEqual(1, inversions(self.A))
        self.assertEqual(5, inversions(self.B))
        self.assertEqual(2, inversions(self.C))

if __name__=='__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise