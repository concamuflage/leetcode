# test_word_pattern.py
import unittest
from lc_290 import Solution

sol = Solution()

class TestWordPattern(unittest.TestCase):

    def test_case1(self):
        # pattern = "abba", s = "dog cat cat dog" -> True
        self.assertTrue(sol.wordPattern("abba", "dog cat cat dog"))

    def test_case2(self):
        # pattern = "abba", s = "dog cat cat fish" -> False
        self.assertFalse(sol.wordPattern("abba", "dog cat cat fish"))

    def test_case3(self):
        # pattern = "aaaa", s = "dog cat cat dog" -> False
        self.assertFalse(sol.wordPattern("aaaa", "dog cat cat dog"))
    
    # def test_case4(self):
    #     # pattern = "aaaa", s = "dog cat cat dog" -> False
    #     self.assertTrue(sol.wordPattern("", ""))
    
    def test_case5(self):
        # pattern = "aaaa", s = "dog cat cat dog" -> False
        self.assertTrue(sol.wordPattern("a", "apple"))

if __name__ == "__main__":
    unittest.main(verbosity=2)