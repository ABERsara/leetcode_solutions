# Last updated: 5/11/2025, 5:21:39 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def valid_BST(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return (valid_BST(node.left, low, node.val) and
                    valid_BST(node.right, node.val, high))
        
        return valid_BST(root)
        