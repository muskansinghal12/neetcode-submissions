class Solution:
    def dfs(self, grid, i, j,n,m):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0": 
            return
        grid[i][j] = "0"
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        for x,y in directions:
            self.dfs(grid,i+x,j+y,n,m)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j, n, m)
        return count

        