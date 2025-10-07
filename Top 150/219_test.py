# test_219_contains_nearby_duplicate.py
import unittest
from lc_219 import Solution   # change the import if your filename is different

sol = Solution()

class TestContainsNearbyDuplicate(unittest.TestCase):

    def test_case1(self):
        # nums = [1,2,3,1], k = 3 -> True
        self.assertTrue(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_case2(self):
        # nums = [1,0,1,1], k = 1 -> True
        self.assertTrue(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_case3(self):
        # nums = [1,2,3,1,2,3], k = 2 -> False
        self.assertFalse(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

if __name__ == "__main__":
    unittest.main(verbosity=2)