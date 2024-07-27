# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        root = head
        stack = []
        n = 0
        while root:
            stack.append(root.val)
            root = root.next
        i = 0
        while head:
            if i % 2 != 0:
                head.val= stack.pop()
            else:
                head.val = stack.pop(0)
            head = head.next
            i+=1
        return root            