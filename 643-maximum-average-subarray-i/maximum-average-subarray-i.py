class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        print(res/k)
        temp = res
        for i in range(k, len(nums)):
            temp +=  nums[i]
            temp -= nums[i-k]
            res = max(temp, res)
        return res / k