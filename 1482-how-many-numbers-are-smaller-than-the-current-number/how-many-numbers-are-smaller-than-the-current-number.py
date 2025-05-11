class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = nums.copy()
        k.sort()
        temp = {}
        res = []
        print(k,nums)
        for i, j in enumerate(k):
            if j not in temp:
                temp[j] = i
        print(temp)
        for i in nums:
            res.append(temp[i])

        return res