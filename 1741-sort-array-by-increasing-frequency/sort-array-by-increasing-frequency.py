class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numfreq = Counter(nums)
        nums.sort(key=lambda x: (numfreq[x],-x))
        return nums