# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        curr = head
        total = 0
        while curr:
            curr = curr.next
            total += 1
        print(total)
        c = total - n
        if c == 0:
            return head.next
        total = 0
        curr = head
        while curr.next and total != c - 1:
            curr = curr.next
            total += 1
        print('cur', curr.next.val if curr.next else "ooo")
        if curr and curr.next:
            curr.next = curr.next.next
        print(curr.next)
        return head