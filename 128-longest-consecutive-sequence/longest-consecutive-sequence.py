class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                size = 1
                while size + i in nums:
                    size+=1
                res = max(size,res)
        return res