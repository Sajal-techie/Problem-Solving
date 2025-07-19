class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        table = defaultdict(int)
        temp = 0
        print(table)
        for i in range(k):
            table[nums[i]] += 1
            temp += nums[i]
        # print(table)
        if len(table) == k:
            res = temp
        print(res, temp)
        for i in range(k, len(nums)):
            table[nums[i]] += 1
            table[nums[i-k]] -= 1
            temp += nums[i]
            temp -= nums[i-k]
            if table[nums[i-k]] == 0:
                del table[nums[i-k]]
            if len(table) == k:
                res = max(temp, res)
        print(temp)
        return res