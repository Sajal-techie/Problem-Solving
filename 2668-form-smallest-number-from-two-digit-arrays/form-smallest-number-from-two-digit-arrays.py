class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = list(set(nums1).intersection(set(nums2)))
        if common:
            return min(common)
        num1 = min(nums1)
        num2 = min(nums2)
        if num1 > num2:
            num1, num2 = num2, num1
        return int(f"{num1}{num2}")