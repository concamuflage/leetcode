import unittest
from lc_13 import Solution

sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        s = "III"
        k = sol.romanToInt(s)
        self.assertEqual(3,k)

    
    def test_two(self):
        s = "LVIII"
        k = sol.romanToInt(s)
        self.assertEqual(58,k)
    
    def test_three(self):
        s = "MCMXCIV"
        k = sol.romanToInt(s)
        self.assertEqual(1994,k)

if __name__ == "__main__":
    unittest.main()