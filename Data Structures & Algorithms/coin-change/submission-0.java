class Solution {
    public int coinChange(int[] coins, int amount) 
    {
        
        int ans = coinChangeHelper(coins,amount,coins.length-1);
        return ans == Integer.MAX_VALUE?-1:ans;
        
    }
    public int coinChangeHelper(int[] coins, int target, int index){
        if(target == 0) return 0;
        if(index < 0 || target<0) return Integer.MAX_VALUE;
        int added = 0;
        int not_added = coinChangeHelper(coins,target,index-1);
        
        added = coinChangeHelper(coins,target-coins[index],index);
        if(added != Integer.MAX_VALUE){
                added++;
        }
        return Math.min(added,not_added);
         
    }
}
