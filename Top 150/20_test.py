# test_solution.py
import unittest
from lc_20 import Solution

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # Examples from the prompt
    def test_example1(self):
        self.assertFalse(self.sol.isValid("){"))

    def test_example2(self):
        self.assertTrue(self.sol.isValid("()[]{}"))

    def test_example3(self):
        self.assertFalse(self.sol.isValid("(]"))

    def test_example4(self):
        self.assertTrue(self.sol.isValid("([)]") is False)  # Example 5 in image is false
        # The image’s Example 4 shows "([)]"? If it instead was "([{}])", use True.

    def test_example5(self):
        self.assertFalse(self.sol.isValid("([)]"))

    # Extra edge cases
    def test_empty_string(self):
        self.assertTrue(self.sol.isValid(""))

    def test_single_char(self):
        self.assertFalse(self.sol.isValid("("))

    def test_long_valid(self):
        self.assertTrue(self.sol.isValid("{[()()]}[](()[])"))

    def test_long_invalid(self):
        self.assertFalse(self.sol.isValid("{[(])}"))

if __name__ == "__main__":
    unittest.main()