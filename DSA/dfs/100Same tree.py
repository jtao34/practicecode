# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node_1, node_2):
            if not node_1 and not node_2:
                return True
            elif not node_1 or not node_2:
                return False
            else:
                if node_1.val != node_2.val:
                    return False
                return dfs(node_1.left, node_2.left) and dfs(node_1.right, node_2.right)
        return dfs(p, q)