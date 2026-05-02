#O(n! * n2)
class Solution:
    def canAttack(self, n, i, j, board):
        #horizontal
        # print("horizontal")
        for col in range(n):
            if board[i][col] == 'Q':
                return True
        #vertical
        # print("vertical")
        for row in range(n):
            if board[row][j] == 'Q':
                return True
        #diagonal
        # print("diagonal")
        #top_left
        row = i-1
        col = j-1
        while row>=0 and col>=0:
            if board[row][col] == 'Q':
                return True
            row -= 1
            col -= 1
        #bottom-right
        row = i+1
        col = j+1
        while row<n and col<n:
            if board[row][col] == 'Q':
                return True
            row += 1
            col += 1
        #top-right
        row = i-1
        col = j+1
        while row>=0 and col<n:
            if board[row][col] == 'Q':
                return True
            row -= 1
            col += 1
        #bottom-left
        row = i+1
        col = j-1
        while row<n and col>=0:
            if board[row][col] == 'Q':
                return True
            row += 1
            col -= 1 
        return False
    def helper(self, n, board, ans, queens, row):
        # print(queens)
        # print(row) 
        if queens == 0:
            # print(board)
            temp = []
            for i in range(n):
                temp.append("".join(board[i]))
            ans.append(temp)
            return
        for j in range(n):
            if board[row][j] != 'Q' and not self.canAttack(n,row,j,board):
                board[row][j]='Q'
                self.helper(n,board,ans,queens-1,row+1)
                board[row][j]='.'


        
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [['.']*n]*n
        board = [['.'] * n for _ in range(n)]
        ans = []
        # print(board)
        self.helper(n,board,ans,n,0)
        return ans
        