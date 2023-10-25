# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        limit = -10000
        self.cnt = 0
        def dfs(node, limit):
            #nonlocal cnt
            if not node:
                return
            if node.val >= limit:
                limit = node.val
                self.cnt += 1
            dfs(node.left, limit)
            dfs(node.right, limit)
        dfs(root, limit)
        return self.cnt