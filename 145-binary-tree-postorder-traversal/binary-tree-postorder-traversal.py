# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        def postorder(res, root):
            if root.left:
                postorder(res, root.left)
            if root.right:
                postorder(res, root.right)
            res.append(root.val)
        
        res = []
        postorder(res, root)
        return res