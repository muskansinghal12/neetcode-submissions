class Solution {
    public int uniquePaths(int m, int n) {
        return uniquePathsHelper(0,0,m,n);
    }
    public int uniquePathsHelper(int i, int j, int m , int n){
        if(i == m-1 && j == n-1){
            return 1;
        }
        if(i<0 || j < 0 || i >= m || j >= n) return 0;

        return uniquePathsHelper(i+1,j,m,n)+uniquePathsHelper(i,j+1,m,n);

    }
}
