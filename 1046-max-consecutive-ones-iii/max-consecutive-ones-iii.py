class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = l = z = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
                while z > k and l <= i:
                    if nums[l] == 0:
                        z -= 1
                    l += 1
                res = max(res, (i-l)+1)
            else:
                res = max(res, (i-l)+1)
                
        return res