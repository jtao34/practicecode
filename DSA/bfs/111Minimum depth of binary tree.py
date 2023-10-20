# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        #start from 0!
        count = 0
        while q:
            count += 1
            #traverse every node on that level before count + 1, if any node has no child, return count
            for _ in range(len(q)):
                k = q.popleft()
                if not k.left and not k.right:
                    return count
                else:
                    if k.left:
                        q.append(k.left)
                    if k.right:
                        q.append(k.right)
        return count
                