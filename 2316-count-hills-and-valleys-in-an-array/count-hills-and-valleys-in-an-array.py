class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)-1):
            # print(i, nums[i-1],nums[i], nums[i+1], res)
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                res += 1
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                res += 1
            if nums[i] == nums [i-1] and nums[i] > nums[i+1]:
                l = i
                while l > 0:
                    if nums[l] > nums[l-1]:
                        res += 1
                        break
                    if nums[l] < nums[l-1]:
                        break
                    l -= 1
            if nums[i] == nums[i-1] and nums[i] < nums[i+1]:
                l = i
                while l > 0:
                    if nums[l] < nums[l-1]:
                        res += 1
                        break
                    if nums[l] > nums[l-1]:
                        break
                    l -= 1
        return res