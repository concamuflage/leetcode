# test_valid_anagram.py
import unittest
from lc_242 import Solution

sol = Solution()

class TestValidAnagram(unittest.TestCase):

    def test_case1(self):
        # s = "anagram", t = "nagaram" -> True
        self.assertTrue(sol.isAnagram("anagram", "nagaram"))

    def test_case2(self):
        # s = "rat", t = "car" -> False
        self.assertFalse(sol.isAnagram("rat", "car"))
    
    def test_case3(self):
        # s = "rat", t = "car" -> False
        self.assertTrue(sol.isAnagram("", ""))

    def test_case4(self):
        # s = "rat", t = "car" -> False
        self.assertTrue(sol.isAnagram("a", "a"))


if __name__ == "__main__":
    unittest.main(verbosity=2)