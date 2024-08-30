# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        print(nums)
        index = 0
        currMax = float('-inf')
        for i in range(len(nums)):
            if nums[i] > currMax:
                currMax = nums[i]
                index = i
        left = self.constructMaximumBinaryTree(nums[:index])
        right = self.constructMaximumBinaryTree(nums[index+1:])
        return TreeNode(currMax, left, right)