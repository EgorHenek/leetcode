# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution.deleteNode(node2)

    node = node1
    result = []
    while node:
        result.append(node.val)
        node = node.next

    assert result == [4, 1, 9]
