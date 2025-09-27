# test_valid_palindrome.py
import unittest
from lc_125 import Solution

sol = Solution()

class TestValidPalindrome(unittest.TestCase):

    def test_numbers(self):
        self.assertTrue(sol.isPalindrome("0P"))
        self.assertFalse(sol.isPalindrome("123421"))

if __name__ == "__main__":
    unittest.main(verbosity=2)