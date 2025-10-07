import unittest
from lc_112 import Solution,TreeNode


sol = Solution()

class Test88(unittest.TestCase):
    
    def test_one(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node1.left = node2
        node1.right = node3
        self.assertFalse(sol.hasPathSum(node1,5))
    
    def test_two(self):
        node1 = None 
        self.assertFalse(sol.hasPathSum(node1,0))
    

    def test_three(self):
        # Build the tree [5,4,8,11,None,13,4,7,2,None,None,None,1]

        # Level 4
        node7 = TreeNode(7)
        node2 = TreeNode(2)
        node1 = TreeNode(1)

        # Level 3
        node11 = TreeNode(11, node7, node2)
        node13 = TreeNode(13)
        node4_right = TreeNode(4, None, node1)

        # Level 2
        node4_left = TreeNode(4, node11)
        node8 = TreeNode(8, node13, node4_right)

        # Root
        root = TreeNode(5, node4_left, node8)
        self.assertTrue(sol.hasPathSum(root,22))


if __name__ == "__main__":
    unittest.main()