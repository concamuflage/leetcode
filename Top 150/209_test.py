import unittest

# If your Solution is defined elsewhere, import it instead.
from lc_209 import Solution


class TestMinSubArrayLen(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_target0(self):
        self.assertEqual(self.sol.minSubArrayLen(0, []), 0)

    def test_empty_target5(self):
        self.assertEqual(self.sol.minSubArrayLen(5, []), 0)


    def test_single_1_1(self):
        self.assertEqual(self.sol.minSubArrayLen(1, [1]), 1)

    def test_two_1_11(self):
        self.assertEqual(self.sol.minSubArrayLen(1, [1,1]), 1)

    def test_two_3_11(self):
        self.assertEqual(self.sol.minSubArrayLen(3, [1,1]), 0)

    def test_two_2_11(self):
        self.assertEqual(self.sol.minSubArrayLen(2, [1,1]), 2)

    def test_example_7_big(self):
        self.assertEqual(self.sol.minSubArrayLen(7, [2,3,1,2,4,3]), 2)

    def test_all_ones_11(self):
        self.assertEqual(self.sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0)

    def test_7_144(self):
        self.assertEqual(self.sol.minSubArrayLen(7, [1,4,4]), 2)

    def test_4_144(self):
        self.assertEqual(self.sol.minSubArrayLen(4, [1,4,4]), 1)

    def test_4_122(self):
        self.assertEqual(self.sol.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]), 2)

    def test_3_122(self):
        self.assertEqual(self.sol.minSubArrayLen(11, [1,2,3,4,5]), 3)

    def test_3_122(self):
        self.assertEqual(self.sol.minSubArrayLen(6, [10,2,3]), 1)

if __name__ == "__main__":
    unittest.main()