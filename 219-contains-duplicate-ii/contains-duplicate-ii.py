class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = {}
        for i in range(len(nums)):
            if nums[i] in hs:
                if abs(hs.get(nums[i]) - i) <= k:
                    return True
                
            hs[nums[i]] = i
        return False