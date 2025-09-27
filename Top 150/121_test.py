import unittest
from lc_121 import Solution

sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        nums = [2,1,2,1,0,1,2]
        k = sol.maxProfit(nums)
        self.assertEqual(2,k)

    # def test_two(self):
    #     nums = [1,2]
    #     k = sol.maxProfit(nums)
    #     self.assertEqual(1,k)
    
    

if __name__ == "__main__":
    unittest.main()