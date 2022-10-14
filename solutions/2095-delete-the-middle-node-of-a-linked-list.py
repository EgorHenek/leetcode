class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return None

        count = 1
        current = head
        result = head
        while current.next:
            count += 1
            current = current.next

        middle = count // 2
        for _ in range(0, middle - 1):
            result = result.next

        result.next = result.next.next
        return head


if __name__ == "__main__":
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(7)
    node5 = ListNode(1)
    node6 = ListNode(2)
    node7 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    result = []
    node = solution.deleteMiddle(node1)
    while node:
        result.append(node.val)
        node = node.next

    assert [1, 3, 4, 1, 2, 6]
