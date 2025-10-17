from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._recurTree(nums)
    def _recurTree(self,nums: List[int]):
        if len(nums) == 3:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            root.right = TreeNode(nums[2])
            return root
        elif(len(nums) == 2):
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            root.right = None 
        elif(len(nums) == 1):
            root = TreeNode(nums[0])
            root.left = None
            root.right = None 
        elif(len(nums) == 0):
            root = None 
        else:
            root_index = len(nums) // 2
            left_array = nums[0:root_index]
            right_array = nums[root_index+1:]
            root = TreeNode(nums[root_index])
            root.left = self._recurTree(left_array)
            root.right = self._recurTree(right_array)
        return root
    

sol = Solution()
array = [-10,-3,0,5,9]
root = sol.sortedArrayToBST(array)

print()
        
        


        
