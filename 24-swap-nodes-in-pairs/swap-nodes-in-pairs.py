# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummynode = ListNode(0)
        dummynode.next = head
        tail = dummynode 

        while head and head.next :
            temp = head.next.next

            tail.next = head.next
            head.next.next = head
            head.next = temp

            tail = head
            head = temp
        
        return dummynode.next