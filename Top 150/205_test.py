import unittest
from lc_205 import Solution

sol = Solution()

class TestIsomorphic(unittest.TestCase):
    
    def test_badc_baba_false(self):
        s = "badc"
        t = "baba"
        result = sol.isIsomorphic(s, t)
        self.assertFalse(result)

    def test_empty_strings_true(self):
        s = ""
        t = ""
        self.assertTrue(sol.isIsomorphic(s, t))
    
    def test_single_char_true(self):
        s = "a"
        t = "b"
        self.assertTrue(sol.isIsomorphic(s, t))

    def test_title_paper_true(self):
        s = "title"
        t = "paper"
        self.assertTrue(sol.isIsomorphic(s, t))
    
    def test_foo_bar_false(self):
        s = "foo"
        t = "bar"
        self.assertFalse(sol.isIsomorphic(s, t))


if __name__ == "__main__":
    unittest.main(verbosity=2)