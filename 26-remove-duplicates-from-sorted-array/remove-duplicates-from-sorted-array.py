class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = nums.copy()
        temp = []
        for i in k:
            if i not in temp:
                temp.append(i)
        nums[:] = temp
        return len(list(set(nums)))
