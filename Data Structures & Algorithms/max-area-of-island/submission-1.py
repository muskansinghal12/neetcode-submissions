class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid,i,j,n,m))
        return ans

                    
    
    def dfs(self, grid, i, j, n, m):
        grid[i][j] = 0
        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        area = 1
        for x, y in directions:
            new_x = x+i
            new_y = y+j
            if new_x>=0 and new_y>=0 and new_x<n and new_y<m and grid[new_x][new_y] == 1:
                # print("entered")
                area += self.dfs(grid, new_x, new_y, n, m)
            # else:
            #     return self.dfs(grid, new_x, new_y, n, m)
        return area


        