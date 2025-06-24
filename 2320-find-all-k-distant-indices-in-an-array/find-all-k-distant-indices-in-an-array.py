class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indx = [x for x in range(len(nums)) if nums[x] == key]
        print(indx)
        res = set()
        for i in range(len(nums)):
            for j in indx:
                if abs(i - j) <= k:
                    res.add(i)
        return sorted(list(res))