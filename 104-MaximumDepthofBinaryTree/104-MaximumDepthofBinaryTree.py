# Last updated: 4/28/2025, 2:42:23 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        from collections import deque

        q = deque([root])
        depth = 0

        while q:
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

        return depth
        