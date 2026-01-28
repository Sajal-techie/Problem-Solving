class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        j = len(nums)-1
        res = []
        for i in range(len(nums)):
            if i >= j:
                break
            res.append(nums[i]+nums[j])
            j-=1
        return max(res)