class Solution {
    public int maxProfit(int[] prices) 
    {
        int max_profit = 0;
        int n = prices.length;
        int current_max = prices[n-1];
        for(int i = n-2;i>=0;i--){
            current_max = Math.max(current_max,prices[i]);
            max_profit = Math.max(max_profit,current_max-prices[i]);
        }
        return max_profit;
    }
}
