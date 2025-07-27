class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    
        n = len(nums)
        f = [False] * (n + 1)
        for i in nums:
            if i > 0 and i <= n:
                f[i] = True
        for j in range(1, n + 1):
            if not f[j]:
                return j
        return n + 1 