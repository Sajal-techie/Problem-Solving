class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = res = 0
        for i in nums:
            if i != 0:
                count = 0
            else:
                count += 1
                res += count
        return res