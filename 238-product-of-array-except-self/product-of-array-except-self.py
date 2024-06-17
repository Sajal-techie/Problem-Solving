class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        left = 1
        right = 1
        for i in range(1,len(nums)):
            left *= nums[i-1]
            prod[i] = left 
        print(prod)
        for j in range(len(nums)-2,-1,-1):
            right= right * nums[j+1]
            prod[j]*=right

        return prod