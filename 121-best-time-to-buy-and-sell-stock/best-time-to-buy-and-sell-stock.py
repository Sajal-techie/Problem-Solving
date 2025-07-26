class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = res = 0
        curr_min = float('inf')
        dp = [0] * len(prices)
        for i in range(len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            dp[i] = prices[i] - curr_min
        return max(dp) if max(dp) > 0 else 0