class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = i = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
            else:
                temp = z = 0
                while i < len(nums) and nums[i] == 0:
                    z += 1
                    temp = max(temp, (z*(z+1))/2)
                    i += 1
                res += temp
        return int(res)