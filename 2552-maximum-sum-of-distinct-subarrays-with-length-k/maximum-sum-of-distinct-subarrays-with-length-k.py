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
                while nums[l] != nums[i]:
                    curr -= nums[l]
                    elem.remove(nums[l])
                    l += 1
                
                l += 1
        return max_sum