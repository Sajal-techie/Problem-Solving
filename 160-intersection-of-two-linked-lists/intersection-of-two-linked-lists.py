# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set1 = set()
        set2 = set()
        curr1 = headA
        curr2 = headB
        while curr1 or curr2:
            if curr1:
                set1.add(curr1)
            if curr2:
                set2.add(curr2)
            if curr1 in set2:
                return curr1
            if curr2 in set1:
                return curr2
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return None
        