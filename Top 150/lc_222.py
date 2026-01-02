from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # check left depth
        left_depth = 1
        left_node = root.left
        while left_node is not None:
            left_node = left_node.left
            left_depth += 1
        # check right depth
        right_depth = 1
        right_node = root.right
        while right_node is not None:
            right_node = right_node.right
            right_depth += 1
        if right_depth == left_depth:
            return (1 << right_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

sol = Solution()
node1 = TreeNode(1)
print(sol.countNodes(None)) # 0
print(sol.countNodes(node1)) # 1

node1 = TreeNode(1)
node1.left = TreeNode(2)


print(sol.countNodes(node1)) # 2
node1.right = TreeNode(3)
print(sol.countNodes(node1)) # 3

node1.left.left = TreeNode(4)
print(sol.countNodes(node1)) # 4

node1.left.right = TreeNode(5)
print(sol.countNodes(node1)) # 5

node1.right.left = TreeNode(6)
print(sol.countNodes(node1)) # 6

node1.right.right = TreeNode(7)
print(sol.countNodes(node1)) # 7


        