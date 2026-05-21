from collections import deque
class Solution:
            
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append([i,j,0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            print("entered")
            i,j,val = queue.popleft()
            for x,y in directions:
                new_x = x + i
                new_y = y + j
                if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and grid[new_x][new_y] > 0:
                    if val+1 < grid[new_x][new_y]:
                        grid[new_x][new_y] = val+1
                        queue.append([new_x,new_y,val+1])



        