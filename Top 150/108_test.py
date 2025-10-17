import unittest
from lc_108 import Solution,TreeNode

sol = Solution()

class Test104(unittest.TestCase):
    
        

    def test_two(self):
        sol = Solution()
        array = [-10,-3,0]
        root = sol.sortedArrayToBST(array)



    def test_tree(self):
        sol = Solution()
        array = [-10,-3]
        root = sol.sortedArrayToBST(array)

    def test_four(self):
        sol = Solution()
        array = [-10]
        root = sol.sortedArrayToBST(array)

    def test_four(self):
        sol = Solution()
        array = []
        root = sol.sortedArrayToBST(array)
    
    def test_one(self):
        sol = Solution()
        array = [-10,-3,0,5,9]
        root = sol.sortedArrayToBST(array)



if __name__ == "__main__":
    unittest.main()