class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = [x for x,y in counter.items() if y> len(nums)/3]
        return result