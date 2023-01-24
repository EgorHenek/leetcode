# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val is not q.val:
            return False
        return self.isSameTree(p.left, q.left,) and self.isSameTree(
            p.right,
            q.right,
        )


if __name__ == "__main__":
    solution = Solution()

    p11 = TreeNode(1)
    p12 = TreeNode(2)
    p13 = TreeNode(3)
    p11.left = p12
    p11.right = p13

    q11 = TreeNode(1)
    q12 = TreeNode(2)
    q13 = TreeNode(3)
    q11.left = q12
    q11.right = q13

    assert solution.isSameTree(p11, q11) is True

    p11.right = None
    q11.left = None

    assert solution.isSameTree(p11, q11) is False

    p11.right = p13
    q11.left = q12
    p11.right.val = 1
    q11.left.val = 1
    q11.right.val = 2

    assert solution.isSameTree(p11, q11)
