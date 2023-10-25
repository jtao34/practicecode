# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #bottom up
        if root == None or root == p or root == q:
            return root
        #always pass info to same root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        #check the info from left and right subtree
        #determines what info should root carry
        #vals are unique
        if left and right:
            return root
        else:
            if not left:
                return right
            return left
