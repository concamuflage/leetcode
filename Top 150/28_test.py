# test_strstr.py
import unittest
from lc_28 import Solution

sol = Solution()

class TestStrStr(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(sol.strStr("sadbutsad", "sad"), 0)   # example 1
        self.assertEqual(sol.strStr("leetcode", "leeto"), -1) # example 2

    def test_empty_needle(self):
        # LeetCode spec: empty needle returns 0
        self.assertEqual(sol.strStr("abc", ""), 0)
        self.assertEqual(sol.strStr("", ""), 0)

    def test_equal_strings(self):
        self.assertEqual(sol.strStr("abc", "abc"), 0)

    def test_not_found(self):
        self.assertEqual(sol.strStr("aaaaa", "bba"), -1)
        self.assertEqual(sol.strStr("", "a"), -1)

    def test_single_char(self):
        self.assertEqual(sol.strStr("a", "a"), 0)
        self.assertEqual(sol.strStr("abc", "c"), 2)
        self.assertEqual(sol.strStr("abc", "d"), -1)

    def test_overlap_occurrences(self):
        # overlapping patterns: first occurrence still at 0
        self.assertEqual(sol.strStr("aaa", "aa"), 0)
        self.assertEqual(sol.strStr("aaaa", "aaa"), 0)

    def test_middle_occurrence(self):
        self.assertEqual(sol.strStr("abcxabcdabxabcdabcdabcy", "abcdabcy"), 15)

    def test_case_sensitive(self):
        self.assertEqual(sol.strStr("Abcabc", "abc"), 3)
        self.assertEqual(sol.strStr("Abcabc", "Abc"), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)