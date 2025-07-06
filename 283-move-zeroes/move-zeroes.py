class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while l < len(nums) and r < len(nums):
            if nums[r] != 0:
                r += 1
            elif nums[l] == 0:
                l += 1
            else:
                if l <= r:
                    l += 1
                else:
                    nums[r], nums[l] = nums[l], nums[r]
                    l += 1
                    r += 1
