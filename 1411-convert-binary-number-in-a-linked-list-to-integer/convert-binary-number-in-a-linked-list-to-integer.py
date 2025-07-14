# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        val = []
        while head is not None:
            val.append(head.val)
            head = head.next
        print(val)
        res = 0
        val = val[::-1]
        for i in range(0, len(val)):
            res += ( val[i] * (2**i))
        return res