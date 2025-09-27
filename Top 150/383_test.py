# test_ransom_note.py
import unittest
from lc_383 import Solution

sol = Solution()

class TestRansomNote(unittest.TestCase):

    # def test_case1(self):
    #     # ransomNote = "a", magazine = "b" -> False
    #     self.assertFalse(sol.canConstruct("a", "b"))

    # def test_case2(self):
    #     # ransomNote = "aa", magazine = "ab" -> False
    #     self.assertFalse(sol.canConstruct("aa", "ab"))

    def test_case3(self):
        # ransomNote = "aa", magazine = "aab" -> True
        self.assertTrue(sol.canConstruct("aa", "aab"))

    # A few helpful extras
    def test_empty_note(self):
        self.assertTrue(sol.canConstruct("", "anything"))

    def test_empty_magazine(self):
        self.assertFalse(sol.canConstruct("a", ""))

    def test_exact_multiset_match(self):
        self.assertTrue(sol.canConstruct("abc", "cba"))

if __name__ == "__main__":
    unittest.main(verbosity=2)