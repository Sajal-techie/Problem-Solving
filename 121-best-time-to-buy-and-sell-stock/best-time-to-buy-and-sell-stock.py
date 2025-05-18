class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = res = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                prof = prices[right] - prices[left]
                res = max(prof, res)
            else:
                left = right
            right += 1
        return res