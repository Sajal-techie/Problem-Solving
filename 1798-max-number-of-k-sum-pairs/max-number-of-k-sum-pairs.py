class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        table = {}
        for i in range(len(nums)):
            val = k - nums[i]
            if val in table and table.get(val, 0) > 0:
                count += 1
                table[val] = table.get(val,1) - 1 
            else:
                table[nums[i]] = table.get(nums[i],0) + 1
        return count