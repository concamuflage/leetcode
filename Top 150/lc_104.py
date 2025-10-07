from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._recur_count(0,root)
    
    def _recur_count(self,count:int,node:Optional[TreeNode]):
        if node is None:
            return count 
        left = node.left
        right = node.right
        count += 1
        count1 = self._recur_count(count, left)
        count2 = self._recur_count(count, right)
        return max(count1,count2)


        
