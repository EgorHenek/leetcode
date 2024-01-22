class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True