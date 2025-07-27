class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = prev = prev_min =  0
        curr_min = float('inf')
        for i in prices:
            if i < curr_min:
                curr_min = i
            if i > prev and i - curr_min > 0:
                res -= (prev - prev_min)
                val = i - curr_min
                res += val
                prev = i
                prev_min = curr_min
            else:
                curr_min = i
                prev = 0
                prev_min = 0
        return res