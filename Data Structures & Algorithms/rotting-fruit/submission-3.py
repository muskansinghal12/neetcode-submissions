from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,2))
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            i, j, time = queue.popleft()
            for x,y in directions:
                new_x = x+i
                new_y = y+j
                if new_x>=0 and new_y>=0 and new_x < n and new_y < m and grid[new_x][new_y] >= 1:
                    if grid[new_x][new_y] == 1 or time+1 < grid[new_x][new_y]:
                        grid[new_x][new_y] = time+1
                        queue.append((new_x,new_y,time+1))
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                ans = max(ans, grid[i][j])
        return 0 if ans == 0 else ans-2
                
                        
        