from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # the following solution used a list to save all the numbers in order
# # then slide a window of 2 and find a minimum difference.

# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         numbers = []
#         self.inorder(root,numbers)
#         slow = 0
#         fast = slow + 1
#         minimum = float("inf")
#         while slow <= len(numbers) - 2:
#             slow_number = numbers[slow]
#             fast_number = numbers[fast]
#             difference = abs(slow_number-fast_number)
#             if difference < minimum:
#                 minimum = difference
#             slow += 1
#             fast += 1 
#         return minimum 

#     def inorder(self,root,numbers):
#         if root is None:
#             return 
#         if root.left is not None:
#             self.inorder(root.left,numbers)
#         numbers.append(root.val)
#         if root.right is not None:
#             self.inorder(root.right,numbers)

# the following doesn't use the list.

class Solution:
    def __init__(self):
        self.prev = None
        self.minimum = float("inf")
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self._inorder(root)
        return self.minimum


    def _inorder(self,root):
        if root is None:
            return 
        if root.left is not None:
            self._inorder(root.left)
        if self.prev is not None:
            self.minimum = min(self.minimum, abs(self.prev- root.val))
        self.prev = root.val
        if root.right is not None:
            self._inorder(root.right)