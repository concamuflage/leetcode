# test_strstr.py
import unittest
from lc_54 import Solution

sol = Solution()

class TestStrStr(unittest.TestCase):

    def test_one(self):
        sol = Solution()
        m = [[1,2,3],[4,5,6],[7,8,9]]
        result = sol.spiralOrder(m)
        self.assertEqual(result,[1,2,3,6,9,8,7,4,5])
    def test_two(self):
        sol = Solution()
        m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        result = sol.spiralOrder(m)
        self.assertEqual(result,[1,2,3,4,8,12,11,10,9,5,6,7])
    def test_three(self):
        sol = Solution()
        m = [[1,2,3,4,5],[5,6,7,8,9],[9,10,11,12,13],[1,2,3,4,5]]
        result = sol.spiralOrder(m)
        self.assertEqual(result, [1,2,3,4,5,9,13,5,4,3,2,1,9,5,6,7,8,12,11,10])

if __name__ == "__main__":
    unittest.main(verbosity=2)