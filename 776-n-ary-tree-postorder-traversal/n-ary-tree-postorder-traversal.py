"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if not node:
            return
        for nod in node.children:
            self.traverse(nod, result )
        
        result.append(node.val)