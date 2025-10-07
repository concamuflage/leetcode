import unittest
from lc_1 import Solution  # adjust if your file name is different

sol = Solution()

class TestTwoSum(unittest.TestCase):

    def test_case1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(sorted(sol.twoSum(nums, target)), [0, 1])

    def test_case2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(sorted(sol.twoSum(nums, target)), [1, 2])

    def test_case3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(sorted(sol.twoSum(nums, target)), [0, 1])

if __name__ == "__main__":
    unittest.main(verbosity=2)