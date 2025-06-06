# Last updated: 5/7/2025, 2:26:41 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
        
        if q is None and p is None:
            return True
        
        if q is None or p is None:
            return False

        if q.val != p.val:
            return False
        
        return self.isSameTree( p.left, q.left) and self.isSameTree( p.right, q.right)