class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        count =0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j]-nums[i] > count:
                    count = nums[j]-nums[i]
        
        return count if count else -1