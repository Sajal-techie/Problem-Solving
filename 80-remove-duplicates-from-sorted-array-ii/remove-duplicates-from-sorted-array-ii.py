class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = l = count = res = 0
        while i < len(nums):
            # print(f"i={i}, nums[i]={nums[i]}, l={l}, nums[l]={nums[l]}, c={count}, res={res}, nums={nums}")
            if nums[i] != nums[l]:
                if count > 2:
                    nums.pop(l)
                    res += 1
                count = 1
                l = i
                i+=1
            else:
                count += 1
                if count > 2:
                    nums.pop(l)
                    count -= 1
                else:
                    i += 1
        return len(nums)