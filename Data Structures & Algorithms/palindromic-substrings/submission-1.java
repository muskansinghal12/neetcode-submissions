class Solution {
    public int isPalindrome(int i, int j, String s, int[][] dp){
        if(i>j) return 0;
        if(dp[i][j] != -1) return dp[i][j];

        if(s.charAt(i) == s.charAt(j)){
            return dp[i][j] = isPalindrome(i+1,j-1,s,dp);
        }
        return dp[i][j] = 1;
    }
    public int countSubstrings(String s) {
        int n = s.length();
        int count = 0;
        int[][] dp = new int[n][n];
        for(int i = 0;i<n;i++){
            Arrays.fill(dp[i],-1);
        }
        for(int i = 0;i<n;i++){
            for(int j = i;j<n;j++){
                if(isPalindrome(i,j,s,dp) == 0){
                    count++;
                }
            }
        }
        return count;
    }
}
