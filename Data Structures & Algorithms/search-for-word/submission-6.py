class Solution:
    def helper(self, board, i, j, word, word_index):
        if len(word) == word_index:
            return True
        if i<0 or j<0 or i>=len(board) or j >= len(board[0]) or board[i][j] != word[word_index]:
            return False
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        temp = board[i][j]
        board[i][j] = '#'
        for x,y in directions:
            if self.helper(board,i+x,j+y,word,word_index+1):
                return True
        board[i][j] = temp
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self.helper(board,i,j,word,0):
                        return True
        return False
    


        