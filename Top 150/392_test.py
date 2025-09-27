# test_is_subsequence.py
import unittest
from lc_392 import Solution

sol = Solution()

class TestIsSubsequence(unittest.TestCase):

    def test_examples(self):
        self.assertTrue(sol.isSubsequence("abc", "ahbgdc"))   # example 1
        self.assertFalse(sol.isSubsequence("axc", "ahbgdc"))  # example 2

    def test_empty_s(self):
        self.assertTrue(sol.isSubsequence("", "anything"))    # empty s is subsequence
        self.assertTrue(sol.isSubsequence("", ""))

    def test_empty_t(self):
        self.assertFalse(sol.isSubsequence("a", ""))

    def test_same_strings(self):
        self.assertTrue(sol.isSubsequence("abc", "abc"))

    def test_repeated_chars(self):
        self.assertTrue(sol.isSubsequence("aaa", "aaabaa"))
        self.assertTrue(sol.isSubsequence("aaaa", "aaabaa"))

    def test_order_matters(self):
        self.assertFalse(sol.isSubsequence("abc", "acb"))
        self.assertTrue(sol.isSubsequence("ace", "abcde"))

    def test_non_overlapping(self):
        self.assertFalse(sol.isSubsequence("xyz", "abc"))

if __name__ == "__main__":
    unittest.main(verbosity=2)