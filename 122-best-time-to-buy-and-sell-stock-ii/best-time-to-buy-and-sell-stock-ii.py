class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        res = 0
        for i in prices[1:]:
            if i > prev:
                res += i - prev
            prev = i
        return res