# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node, min_value=float('-inf'), max_value=float('inf')):
            if node is None:
                return True
            if min_value < node.val < max_value:
                return isBST(node.left, min_value, node.val) and isBST(node.right, node.val,max_value)
        
        return isBST(root)