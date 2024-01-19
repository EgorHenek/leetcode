# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       values = {}
       while True:
            if head is None:
                return False
            if head in values:
                return True
            values[head] = 1
            head = head.next 