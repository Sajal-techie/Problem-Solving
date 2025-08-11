# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = 1
        n2 = 1
        curr1 = headA
        curr2 = headB
        while curr1.next:
            curr1 = curr1.next
            n1 += 1
        while curr2.next:
            curr2 = curr2.next
            n2 += 1
        print(curr1.val, curr2.val, n1, n2)
        if curr1 and curr2 and curr1 != curr2:
            return None
        if n1 > n2:
            curr = headA
            other = headB
            l = n1
            s = n2
        else:
            curr = headB
            other = headA
            l = n2
            s = n1
        while l != s and curr:
            curr = curr.next
            l -= 1
        print(curr.val, other.val)
        while curr and other:
            if curr == other:
                return curr
            curr = curr.next
            other = other.next
        print("hai")