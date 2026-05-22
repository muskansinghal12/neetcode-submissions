class Solution:
    def helper(self, board, i, j, n, m, visited):
        if i<0 or j < 0 or i >= n or j >= m or visited[i][j] or board[i][j] != "O":
            return 
        visited[i][j] = True
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for x,y in directions:
            self.helper(board, x+i, y+j, n, m, visited)
            
        
         
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = [[False]*m for _ in range(n)]
        #upper row
        for i in range(m):
            if board[0][i] == "O":
                self.helper(board,0,i,n,m,visited)
        #left col
        for i in range(n):
            if board[i][0] == "O":
                self.helper(board,i,0,n,m,visited)
        #bottom row
        for i in range(m):
            if board[n-1][i] == "O":
                self.helper(board,n-1,i,n,m,visited)
        #right col
        for i in range(n):
            if board[i][m-1] == "O":
                self.helper(board,i,m-1,n,m,visited)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"
        


        