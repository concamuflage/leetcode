import unittest
from lc_58 import Solution

sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        s =  "   fly me   to   the moon  "
        k = sol.lengthOfLastWord(s)
        self.assertEqual(4,k)


if __name__ == "__main__":
    unittest.main()