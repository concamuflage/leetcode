import unittest
from lc_26 import Solution

sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        nums = [1,1,2]
        k = sol.removeDuplicates(nums)
        self.assertEqual(2,k)
        self.assertEqual(nums[0:k],[1,2])
    
    def test_two(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        k = sol.removeDuplicates(nums)
        self.assertEqual(5,k)
        self.assertEqual(nums[0:k],[0,1,2,3,4])

if __name__ == "__main__":
    unittest.main()