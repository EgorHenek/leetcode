# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast:
            if slow.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
            if slow is fast:
                return True
        return False