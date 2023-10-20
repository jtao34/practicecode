# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if not root:
            return res
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                k = q.popleft()
                level.append(k.val)
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
            res.append(level)
        return res
                
            