class Solution {
    public int coinChange(int[] coins, int amount) 
    {
        int n = coins.length;
        int dp[][] = new int[amount+1][n+1];
        for(int i=1;i<=amount;i++){
            for(int j = 0;j<=n;j++){
                dp[i][j] = Integer.MAX_VALUE/2;
            }
        }
        for(int i = 1;i<=amount;i++){
            for(int j = 1;j<=n;j++){
                int not_added = dp[i][j-1];
                int added = Integer.MAX_VALUE/2;
                if(i>=coins[j-1]){
                    added = 1 + dp[i-coins[j-1]][j];
                }
                
                dp[i][j] = Math.min(added,not_added);
            }
        }
        
        int ans = dp[amount][n];
        return ans >= Integer.MAX_VALUE / 2 ? -1 : ans;
        
    }
}