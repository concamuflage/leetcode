from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self._recur_sum(root,targetSum)
    
    def _recur_sum(self,root,target):
        if root is None:
            return False

        # base condition
        if root.left is None and root.right is None: # if root is a leaf
            if root.val == target:
                return True 
            else:
                return False
        else: # root not a leaf
            new_target = target - root.val 
            return self._recur_sum(root.left,new_target) or self._recur_sum(root.right,new_target)

        