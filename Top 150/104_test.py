import unittest
from lc_104 import Solution,TreeNode

sol = Solution()

class Test104(unittest.TestCase):
    
    def test_one(self):
        node7 = TreeNode(7)
        node15 = TreeNode(15)
        node20 = TreeNode(20, node15, node7)
        node9 = TreeNode(9, None, None)
        node3 = TreeNode(3, node9, node20)
        length = sol.maxDepth(node3)
        self.assertEqual(length,3)
    
    def test_two(self):
        node3 = TreeNode(3)
        length = sol.maxDepth(node3)
        self.assertEqual(length,1)


    def test_two(self):
        node3 = None
        length = sol.maxDepth(node3)
        self.assertEqual(length,0)



if __name__ == "__main__":
    unittest.main()