# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        #use dfs bottom up?
        if not root:
            return 0

        # Define a recursive DFS function
        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # The depth of the current node is the maximum depth of its children + 1
            return max(left_depth, right_depth) + 1

        # Start the DFS from the root
        return dfs(root)
    
    
        #use dfs top down
        if not root:
            return 0
        res = [0]
        def dfs(root, d, res):
            if not root.left and not root.right:
                res[0] = max(res[0], d)
                return
            if root.left:
                dfs(root.left, d+1, res)
            if root.right:
                dfs(root.right, d+1, res)
        dfs(root, 1, res)
        return res[0]