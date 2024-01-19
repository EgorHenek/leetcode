class Solution:
    def removeElements(
        self,
        head: ListNode | None,
        val: int,
    ) -> ListNode | None:
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return head