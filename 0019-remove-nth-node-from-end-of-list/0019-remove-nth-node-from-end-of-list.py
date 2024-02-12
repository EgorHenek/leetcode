# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode], n: int = 0) -> Optional[ListNode]:
            prev = None
            counter = 0
            while head:
                counter += 1
                next = head.next
                if counter != n:
                    head.next = prev
                    prev = head
                head = next
            return prev
        head = reverse(head)
        return reverse(head, n)
