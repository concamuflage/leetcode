import unittest
from lc_530 import Solution,TreeNode



class Test88(unittest.TestCase):
    
    def test_one(self):

        # Example tree construction:
        #         4
        #       /   \
        #      2     6
        #     / \
        #    1   3
        sol = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        self.assertEqual(sol.getMinimumDifference(root),1)
    def test_two(self):
        sol = Solution()
        # Construct the tree [1, null, 3, 2]
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        self.assertEqual(sol.getMinimumDifference(root),1)
    def test_three(self):
        #     236
        #    /   \
        # 104     701
        #   \        \
        #   227      911
        root = TreeNode(236)
        root.left = TreeNode(104)
        root.right = TreeNode(701)
        root.left.right = TreeNode(227)
        root.right.right = TreeNode(911)
        sol = Solution()
        self.assertEqual(sol.getMinimumDifference(root),9)
    def test_4(self):
        # Construct the tree [5,4,7]
        root = TreeNode(1)
        root.right = TreeNode(2)
        sol = Solution()
        self.assertEqual(sol.getMinimumDifference(root),1)


if __name__ == "__main__":
    unittest.main()