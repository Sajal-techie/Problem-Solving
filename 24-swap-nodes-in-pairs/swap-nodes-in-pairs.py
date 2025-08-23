# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        curr = head
        while curr:
            nxt = curr.next
            if nxt:
                third = nxt.next
                dummy.next = nxt
                dummy = dummy.next
                dummy.next = curr
                dummy = dummy.next
                dummy.next = third
                curr = third
            else:
                dummy.next = curr
                curr = curr.next
        return res.next