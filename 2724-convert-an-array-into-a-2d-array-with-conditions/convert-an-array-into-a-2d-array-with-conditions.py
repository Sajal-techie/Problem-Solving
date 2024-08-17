class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(len(res)):
                if nums[i] not in res[j]:
                    res[j].append(nums[i])
                    break
            else:
                res.append([nums[i]])

        return res