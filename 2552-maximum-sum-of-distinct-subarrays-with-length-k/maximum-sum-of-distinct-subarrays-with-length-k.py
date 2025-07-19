class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr =  max_sum = l = 0
        elem = set()
        for i in range(len(nums)):
            if nums[i] not in elem:
                elem.add(nums[i])
                curr += nums[i]
                
                if i - l + 1 == k:
                    if curr > max_sum:
                        max_sum = curr
                    elem.remove(nums[l])
                    curr -= nums[l]
                    l += 1
            else:
                while nums[i] in elem:
                    elem.remove(nums[l])
                    curr -= nums[l]
                    l += 1
                elem.add(nums[i])
                curr += nums[i]
        return max_sum