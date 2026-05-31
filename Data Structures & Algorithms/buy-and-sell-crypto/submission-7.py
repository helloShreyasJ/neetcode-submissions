class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force, check every possible buy and sell pair
        maxProfit = 0
        L = 0
        R = 1

        while R < len(prices):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            else:
                L = R
            R += 1

        return maxProfit

