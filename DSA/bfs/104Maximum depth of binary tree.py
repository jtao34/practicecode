#definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs code
        if not root:
            return 0
        q = deque()
        q.append(root)
        count = 0
        while q:
            count += 1
            for _ in range(len(q)):
                k = q.popleft()
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
        return count
            
            
            