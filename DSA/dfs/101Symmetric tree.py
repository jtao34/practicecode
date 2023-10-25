# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #bottom up
        def dfs(left_node, right_node):
            if not left_node and not right_node:
                return True
            elif not left_node or not right_node:
                return False
            else:
                if root.left.val != root.right.val:
                    return False
                else:
                    return dfs(left_node.right, right_node.left) and dfs(left_node.left, right_node.right)
        return dfs(root.left, root.right)