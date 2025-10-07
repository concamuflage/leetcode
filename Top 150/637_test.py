# test_is_subsequence.py
import unittest
from lc_637 import Solution,TreeNode

sol = Solution()

class TestIsSubsequence(unittest.TestCase):

    def test_examples(self):
        # Build the tree
        node15 = TreeNode(15)
        node7 = TreeNode(7)
        node9 = TreeNode(9)
        node20 = TreeNode(20, node15, node7)
        root = TreeNode(3, node9, node20)

        self.assertEqual(sol.averageOfLevels(root),[3.00000,14.50000,11.00000])   # example 1


if __name__ == "__main__":
    unittest.main(verbosity=2)