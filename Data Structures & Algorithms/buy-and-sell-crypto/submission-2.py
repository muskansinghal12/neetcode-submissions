class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_price = prices[-1]
        n = len(prices)
        for i in range(n-2,-1,-1):
            max_profit = max(max_profit,max_price-prices[i])
            max_price = max(max_price, prices[i])
        return max_profit
        