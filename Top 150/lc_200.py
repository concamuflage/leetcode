from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # breadth first approach
        visited = {}
        queue = deque()
        queue.appendleft((0,0))
        while queue:
            x,y = queue.popleft()
            current = grid[x][y]
            self.visit(x,y,current,grid,visited,queue)
        return self.count(grid)
    def visit(self,x,y,current,grid,visited,queue):
        visited[(x,y)] = grid[x][y]
        self.explore(x,y,current,grid,visited,queue)

    def explore(self,x,y,current,grid,visited,queue):
        # explore above
        if x -1 >= 0:
            self.explore_node(x-1,y,current,grid,visited,queue)
        # explore below
        if x + 1 <= len(grid) -1:
            self.explore_node(x+1,y,current,grid,visited,queue)
        # explore left
        if y - 1 >=0:
            self.explore_node(x, y-1, current, grid, visited, queue)
        # explore right
        if y + 1 <= len(grid[0])-1:
            self.explore_node(x, y + 1, current, grid, visited, queue)

    def explore_node(self,x,y,current,grid,visited,queue):
        # if this position is already visited and explored
        if (x,y) in visited:
            return
        element = grid[x][y]
        if element == "1" and current in ("1","2"):  # if this node is "1" and the center node is "1" or "2"
            grid[x][y] = "2" # sink the land.
        if (x,y) not in visited:
            queue.append((x,y))
    def count(self,grid):
        count = 0
        for row in grid:
            for element in row:
                if element == "1":
                    count +=1
        return count

sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numIslands(grid)) # 1
for row in grid:
    print(row)
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(sol.numIslands(grid)) # #
for row in grid:
    print(row)