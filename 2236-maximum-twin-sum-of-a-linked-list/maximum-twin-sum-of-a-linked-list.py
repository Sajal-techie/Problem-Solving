# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        max_sum = 0
        prev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        while curr and prev:
            curr_sum = curr.val + prev.val
            max_sum = max(curr_sum, max_sum)
            curr = curr.next
            prev = prev.next
        return max_sum