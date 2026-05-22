class Solution:
    def helper(self, grid, i, j, n, m, visited):
        visited[i][j] = True
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for x, y in directions:
            new_x = i+x
            new_y = j+y
            if new_x >=0 and new_y >= 0 and new_x < n and new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] >= grid[i][j]:
                self.helper(grid, i+x, j+y, n, m, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific_visited = [[False]*m for _ in range(n)]
        atlantic_visited = [[False]*m for _ in range(n)]
        #top_row
        for i in range(m):
            # pacific_visited[0][i] = True
            self.helper(heights,0,i,n,m,pacific_visited)
        
        #left_col
        for i in range(n):
            # pacific_visited[i][0] = True
            self.helper(heights,i,0,n,m,pacific_visited)
        
        #bottom_row
        for i in range(m):
            self.helper(heights,n-1,i,n,m,atlantic_visited)

        #right_col
        for i in range(n):
            self.helper(heights,i,m-1,n,m,atlantic_visited)
        
        ans = []
        for i in range(n):
            for j in range(m):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    ans.append([i,j])
        return ans



        