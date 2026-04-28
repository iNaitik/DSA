class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            profit = prices[r]-prices[l]
            if profit >= 0:
                r += 1
            else:
                l += 1
            max_profit = max(max_profit, profit)
        if max_profit == 0:
            return 0
        else:
            return max_profit