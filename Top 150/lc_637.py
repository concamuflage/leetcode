# Definition for a binary tree node.

from typing import Optional,List
from collections import deque



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        levels = self.getLevels(root)  
        for level in levels:
            average = sum(level)/len(level) 
            averages.append(round(average,5))
        return averages
    
    def getLevels(self, root: Optional[TreeNode]) -> List[List]:

        queue = deque([root])
        levels = []
        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            levels.append(level)

        return levels