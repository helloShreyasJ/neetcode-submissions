class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force, check every possible buy and sell pair
        maxProfit = 0

        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                profit = sell - buy
                maxProfit = max(maxProfit, profit)
        
        return maxProfit
