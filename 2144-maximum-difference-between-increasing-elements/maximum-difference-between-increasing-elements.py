class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        re = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j]-nums[i] > re:
                    re = nums[j]-nums[i]
        
        return re if re else -1