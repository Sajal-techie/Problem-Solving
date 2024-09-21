class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        for i in range(len(nums)):
            leftsum = sum(nums[left:i])
            rightsum = sum(nums[i+1:right])
            if leftsum == rightsum:
                return i

        return -1