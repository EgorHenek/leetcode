# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def get_medium(head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = head, head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        medium = get_medium(head)

        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = head
            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev
        
        reversed_half = reverse_list(medium.next)

        while reversed_half:
            if head.val != reversed_half.val:
                return False
            head = head.next
            reversed_half = reversed_half.next
        return True
        