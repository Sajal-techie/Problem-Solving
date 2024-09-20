class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) -1
        
        maxlen = 0
        curr = 0
        zeros = 0
        i = j = 0
        while i < len(nums) and j < len(nums):
            if nums[j] == 0:
                zeros += 1
                    
            while zeros > 1:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            j += 1
            maxlen = max(maxlen, j-i)
        return maxlen - 1