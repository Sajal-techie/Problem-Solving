# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 1
        curr = list1
        while curr.next is not None:
            if count == a:
                temp = curr
                curr = curr.next
                temp.next = list2
                while temp.next is not None:
                    temp = temp.next
            elif count == b+1:
                temp.next = curr.next
            else:
                curr = curr.next
            count += 1

        return list1