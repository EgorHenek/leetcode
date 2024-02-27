# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def height(root: Optional[TreeNode]) -> None:
            if not root:
                return 0
            nonlocal diameter
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter,  left + right)
            return max(left, right) + 1
        height(root)
        return diameter
        