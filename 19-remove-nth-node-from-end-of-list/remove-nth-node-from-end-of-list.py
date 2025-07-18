# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        root = head
        while root :
            count += 1
            root = root.next
        root = head
        while root:
            count -= 1
            if count == n:
                root.next = root.next.next
                break
            if count < n:
                head = root.next
                break
            root = root.next
        
        return head