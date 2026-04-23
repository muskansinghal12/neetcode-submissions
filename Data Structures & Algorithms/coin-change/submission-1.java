class Solution {
    public int coinChange(int[] coins, int amount) 
    {
        int n = coins.length;
        int dp[][] = new int[amount+1][n+1];
        for(int i = 0;i<=amount;i++){
            Arrays.fill(dp[i],-1);
        }
        
        int ans = coinChangeHelper(coins,amount,coins.length-1,dp);
        return ans == Integer.MAX_VALUE?-1:ans;
        
    }
    public int coinChangeHelper(int[] coins, int target, int index, int[][] dp){
        if(target == 0) return 0;
        if(index < 0 || target<0) return Integer.MAX_VALUE;
        if(dp[target][index] != -1) return dp[target][index];
        int added = 0;
        int not_added = coinChangeHelper(coins,target,index-1,dp);
        
        added = coinChangeHelper(coins,target-coins[index],index,dp);
        if(added != Integer.MAX_VALUE){
                added++;
        }
        return dp[target][index] = Math.min(added,not_added);
         
    }
}
