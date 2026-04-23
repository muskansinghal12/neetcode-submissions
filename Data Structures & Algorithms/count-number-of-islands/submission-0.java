class Solution {
    public int numIslands(char[][] grid) 
    {
        int n = grid.length;
        int m = grid[0].length;
        boolean visited[][] = new boolean[n][m];
        int count = 0;
        for(int i = 0;i<grid.length;i++){
            for(int j = 0;j<grid[i].length;j++){
                if(!visited[i][j] && grid[i][j] == '1'){
                    dfs(grid,visited,i,j);
                    count++;
                }
            }
        }
        return count;
    }
    public void dfs(char[][] grid, boolean visited[][], int i, int j){
        visited[i][j] = true;
        int directions[][] = new int[][]{{-1,0},{1,0},{0,-1},{0,1}};
        for(int[] direction : directions){
            int x = i + direction[0];
            int y = j + direction[1];
            if(x<0 || y<0 || x>=grid.length || y>=grid[i].length || visited[x][y] || grid[x][y] == '0'){
                continue;
            }
            else{
                dfs(grid,visited,x,y);
            }
        }
    }
}
