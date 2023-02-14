# https://leetcode.com/problems/remove-linked-list-elements/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
        self,
        head: ListNode | None,
        val: int,
    ) -> ListNode | None:
        while head and head.val == val:
            head = head.next

        if head is None:
            return None

        temp = head

        while temp.next:
            next_node = temp.next
            if next_node.val == val:
                temp.next = next_node.next
            else:
                temp = temp.next
        return head


if __name__ == "__main__":
    solution = Solution()
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(6)
    t4 = ListNode(3)
    t5 = ListNode(4)
    t6 = ListNode(5)
    t7 = ListNode(6)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    t6.next = t7

    expect = [1, 2, 3, 4, 5]
    result = solution.removeElements(t1, 6)
    if result is not None:
        while True:
            assert result.val == expect.pop(0)
            if result.next is None:
                break
            result = result.next
