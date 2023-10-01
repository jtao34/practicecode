# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ##recursive idea
        ##append value to ans list, to avoid recursion reset ans, has to use helper function and put ans outside 
        #ans = []
        #def inOrder(root, ans):
        #    if not root:
        #        return
        #    inOrder(root.left, ans)
        #    ans.append(root.val)
        #    inOrder(root.right, ans)
        #inOrder(root, ans)
        #return ans
        
        #DFS idea----- Need to memorize this first PLZ!!
        ans = []
        stack = []
        cur = root
        while stack or cur:
            #inOrder(left, ans)
            if cur:
                stack.append(cur)
                cur = cur.left
            #if not cur, first step finish, backtrack and resume prev second step and third step (search right node) 
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans
        
        
        