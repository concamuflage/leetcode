import unittest
from lc_202 import Solution  # adjust if your file name is different

sol = Solution()

class TestTwoSum(unittest.TestCase):

    def test_case0(self):
        self.assertEqual(sol._next_number(50),25)
    def test_case4(self):
        self.assertEqual(sol._next_number(19),82)

    def test_case1(self):
        nums = 19
        self.assertTrue(sol.isHappy(19))

    def test_case2(self):
        nums = 2
        self.assertFalse(sol.isHappy(2))



if __name__ == "__main__":
    unittest.main(verbosity=2)