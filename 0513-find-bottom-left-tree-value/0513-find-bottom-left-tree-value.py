# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        bottom_left_value = 0
        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if not root: return None
            nonlocal max_depth
            nonlocal bottom_left_value
            if depth > max_depth:
                max_depth = depth
                bottom_left_value = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return bottom_left_value