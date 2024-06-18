class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = nums.count(0)
        sk = 0
        while i < (len(nums)-zeros):
            if sk == zeros: break
            if nums[i] == 0:
                nums.append(nums.pop(i))
                sk+=1
            else:
                i+=1