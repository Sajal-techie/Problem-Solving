class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = max(nums)
        ans = 0
        for i in range(k):
            res = res + 1
            ans = ans + res
        return ans - k