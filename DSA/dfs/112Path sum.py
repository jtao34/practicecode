# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cum_sum):
            if not node:
                return False
            cum_sum += node.val
            if not node.left and not node.right:
                if cum_sum == targetSum:
                    return True
                return False
            return dfs(node.left, cum_sum) or dfs(node.right, cum_sum)
        return dfs(root, 0)