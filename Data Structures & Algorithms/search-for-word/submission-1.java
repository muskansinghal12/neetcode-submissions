class Solution {
    public boolean exist(char[][] board, String word) 
    {
        for(int i = 0;i<board.length;i++){
            for(int j = 0;j<board[i].length;j++){
                if(word.charAt(0) == board[i][j]){
                    boolean visited[][] = new boolean[board.length][board[i].length];
                    if(existHelper(board,word,0,i,j,visited))return true;
                }
            }
        }
        return false;
    }
    public boolean existHelper(char[][] board, String word, int s_index, int i, int j, boolean visited[][]){
        if(s_index >= word.length()) return true;
        if(i<0||j<0||i>=board.length||j>=board[i].length || visited[i][j]) return false;
        int directions[][] = new int[][]{{-1,0},{1,0},{0,-1},{0,1}};
        
        visited[i][j] = true;
        if(word.charAt(s_index) == board[i][j]){
            for(int[] direction: directions){
                if(existHelper(board, word,s_index+1,i+direction[0],j+direction[1],visited)){
                    return true;
                }
            } 
        }
        visited[i][j] = false;
              
        
        return false;
    }
}
