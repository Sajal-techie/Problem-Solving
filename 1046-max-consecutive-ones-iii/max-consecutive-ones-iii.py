class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        i = j = 0
        while i < len(nums) and j < len(nums):
            if nums[j] == 0:
                count += 1
            if count <= k:
                res = max(res, j-i)
            else:
                if nums[i] == 0:
                    count -= 1
                i += 1

            j += 1

        return res + 1 if 1 in nums else k