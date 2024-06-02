class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and len(nums2)<=1:
            return nums2[0]
        elif not nums2 and len(nums1)<=1:
            return nums1[0]
        arr3 = nums1 + nums2
        arr3.sort()
        n = len(arr3)
        return (arr3[(n//2)-1] + arr3[n//2]) / 2 if n%2 == 0 else arr3[(n//2) ]