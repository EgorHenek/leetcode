# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        # Find the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list.
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # Check if the first half and the second half are the same.
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True


if __name__ == '__main__':
    solution = Solution()
    h1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    h2 = ListNode(1, ListNode(2))
    assert solution.isPalindrome(h1) is True
    assert solution.isPalindrome(h2) is False
