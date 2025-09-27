import unittest
from lc_169 import Solution

sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        nums = [1,1,2]
        k = sol.majorityElement(nums)
        self.assertEqual(1,k)
    
    def test_two(self):
        nums = [9,9,10,10,9]
        k = sol.majorityElement(nums)
        self.assertEqual(9,k)

if __name__ == "__main__":
    unittest.main()