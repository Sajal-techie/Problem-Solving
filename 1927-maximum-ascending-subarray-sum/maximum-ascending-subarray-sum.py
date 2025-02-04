class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                res = max(temp, res)
                temp = nums[i]
        res = max(temp, res)
        return res
