class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            el = nums.pop(i)
            if el not in nums:
                res.append(el)
            nums.insert(i,el)
        
        return res
