# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        curr = TreeNode()
        new_node = curr
        def inorder(root):
            nonlocal curr
            if not root:
                return 
            inorder(root.left)
            curr.right = TreeNode(root.val)
            curr = curr.right
            inorder(root.right)
        inorder(root)
        return new_node.right

