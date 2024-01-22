# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root: Optional[TreeNode], cur, res) -> None:
            if not root:
                return
            
            cur.append(str(root.val))

            if not root.left and not root.right:
                res.append('->'. join(cur))
            
            dfs(root.left, cur, res)
            dfs(root.right, cur, res)

            cur.pop()
        res = []
        dfs(root, [], res)
        return res
        