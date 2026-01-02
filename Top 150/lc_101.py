from collections import deque
from typing import Optional


# Definition for a binary tree node.
# my own solution:
# put all the nodes on the same level in an array
# check if the resulting array is symmetric.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#         queue = deque()
#         queue.append(root)
#         while queue:
#             level_list = []  # traverse each level first and store the node values in a list.
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node is not root:
#                     if node is None:
#                         level_list.append(None)
#                     else:
#                         level_list.append(node.val)
#                 if node is not None:
#                     queue.append(node.left) # None is also put on to the double ended queue; if not, [None,3 None, 3] not symmetric
#                     queue.append(node.right) # becomes [3,3], symmetric
#             # check if this level is symetric.
#             if not self.isSymmetricList(level_list):
#                 return False
#         return True
#
#     def isSymmetricList(self,list):
#         if len(list) % 2 == 1:
#             return False
#         left = 0
#         right = len(list)-1
#         while left < right:
#             if list[left] == list[right]:
#                 left +=1
#                 right -=1
#             else:
#                 return False
#         return True

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def isMirror(t1, t2):
            if not t1 and not t2: # both of them are none
                return True
            if not t1 or not t2: # one of them is none
                return False
            return t1.val == t2.val and \
                    isMirror(t1.left,t2.right) and \
                    isMirror(t1.right,t2.left)
        return isMirror(root.left,root.right)


sol = Solution()
print(sol.isSymmetric(None)) # true
root = TreeNode(1)
print(sol.isSymmetric(root)) #true
node2 = TreeNode(2)
root.left = node2
print(sol.isSymmetric(root)) #false
# node3 = TreeNode(3)
# root.right = node3
# print(sol.isSymmetric(root) )#false

node3 = TreeNode(2)
root.right = node3
print(sol.isSymmetric(root)) #true



