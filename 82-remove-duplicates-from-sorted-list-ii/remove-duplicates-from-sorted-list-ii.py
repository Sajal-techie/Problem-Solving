# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res
        curr = head
        excluded = set()
        while curr:
            if curr.next:
                if curr.val != curr.next.val and curr.val not in excluded:
                    node = ListNode(curr.val)
                    dummy.next = node
                    dummy = dummy.next
                else:
                    excluded.add(curr.val)
            elif curr.val not in excluded:
                node = ListNode(curr.val)
                dummy.next = node
                dummy = dummy.next
            
            curr = curr.next if curr else None
        return res.next