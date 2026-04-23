class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_price = 0
        length = len(prices)
        for i in range(length-1,-1,-1):
            max_price = max(max_price, prices[i])
            profit = max((max_price-prices[i]),profit)
        return profit
        