# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reserve = 0
        start = result = ListNode()
        while l1 or l2 or reserve:
            summary = reserve
            summary += l1.val if l1 else 0
            summary += l2.val if l2 else 0

            reserve, d = divmod(summary, 10)

            result.next = ListNode(d)
            result = result.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return start.next
        