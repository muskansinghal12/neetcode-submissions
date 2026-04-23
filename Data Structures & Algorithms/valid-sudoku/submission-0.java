class Solution {
    public boolean isValidSudoku(char[][] board) 
    {
        
        //check all the rows
        for(int i = 0;i<9;i++){
            int numbers[] = new int[9];
            for(int j = 0;j<9;j++){
                if(board[i][j] == '.') continue;
                if(numbers[board[i][j] - '1'] > 0){
                    return false;
                }
                else{
                    numbers[board[i][j] - '1']++;
                }
            }
        } 
        //check all the columns
        for(int i = 0;i<9;i++){
            int numbers[] = new int[9];
            for(int j = 0;j<9;j++){
                if(board[j][i] == '.') continue;
                if(numbers[board[j][i] - '1'] > 0){
                    return false;
                }
                else{
                    numbers[board[j][i] - '1']++;
                }
            }
        } 
        for(int i = 0;i<9;i=i+3){
            for(int j = 0;j<9;j=j+3){
                int numbers[] = new int[9];
                for(int k = i;k<i+3;k++){
                    for(int l = j;l<j+3;l++){
                        if(board[k][l] == '.') continue;
                        if(numbers[board[k][l] - '1'] > 0){
                            return false;
                        }
                        else{
                            numbers[board[k][l] - '1']++;
                        }

                    }
                }
            }
        }   
        return true;   
    }
}
