# test_summary_ranges.py
import unittest
from lc_228 import Solution   # change filename if needed

sol = Solution()

class TestSummaryRanges(unittest.TestCase):

    def test_example1(self):
        nums = [0,1,2,4,5,7]
        expected = ["0->2","4->5","7"]
        self.assertEqual(sol.summaryRanges(nums), expected)

    def test_example2(self):
        nums = [0,2,3,4,6,8,9]
        expected = ["0","2->4","6","8->9"]
        self.assertEqual(sol.summaryRanges(nums), expected)

    # a couple of quick edges
    def test_empty(self):
        self.assertEqual(sol.summaryRanges([]), [])

    def test_singleton(self):
        self.assertEqual(sol.summaryRanges([5]), ["5"])

if __name__ == "__main__":
    unittest.main(verbosity=2)