import unittest
from lc_27 import Solution

sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        nums = [3,2,2,3]
        val = 3
        k = sol.removeElement(nums,val)
        self.assertEqual(2,k)
        for index in range(k):
            self.assertNotEqual(nums[index],val)
    
    def test_two(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        k = sol.removeElement(nums,val)
        self.assertEqual(5,k)
        for index in range(k):
            self.assertNotEqual(nums[index],val)
    
    def test_two(self):
        nums = [1]
        val = 1
        k = sol.removeElement(nums,val)
        self.assertEqual(1,k)
        for index in range(k):
            self.assertNotEqual(nums[index],val)