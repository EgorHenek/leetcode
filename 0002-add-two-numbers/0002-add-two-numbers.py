# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reserve = 0
        start = result = ListNode()
        while l1 or l2:
            summary = reserve
            if l1:
                summary += l1.val
            if l2:
                summary += l2.val
            result.val = summary % 10
            reserve = summary // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2:
                result.next = ListNode()
                result = result.next
        if reserve:
            result.next = ListNode(reserve)
        return start
        