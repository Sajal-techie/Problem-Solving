class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        first = float('inf')
        second = float('inf')
        third = float('inf')
        if n < 3: return False
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True