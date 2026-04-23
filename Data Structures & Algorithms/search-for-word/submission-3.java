class Solution {
    public boolean exist(char[][] board, String word) 
    {
        int n = board.length;
        int m = board[0].length;
        boolean visited[][] = new boolean[n][m];
        for(int i = 0;i<board.length;i++){
            for(int j = 0;j<board[i].length;j++){
                if(existHelper(board,word,0,i,j,visited))return true;
            }
        }
        return false;
    }
    public boolean existHelper(char[][] board, String word, int s_index, int i, int j, boolean visited[][]){
       
        if(i<0||j<0||i>=board.length||j>=board[i].length || visited[i][j]) return false;
        if(word.charAt(s_index) != board[i][j]) return false;
        if(s_index == word.length()-1) return true;
        
        
        int directions[][] = new int[][]{{-1,0},{1,0},{0,-1},{0,1}};
        visited[i][j] = true;
        for(int[] direction: directions){
            if(existHelper(board, word,s_index+1,i+direction[0],j+direction[1],visited)){
                return true;
            }
        } 
        visited[i][j] = false;
        return false;
    }
}
