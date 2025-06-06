# Last updated: 5/11/2025, 5:22:43 PM
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
        self.prev = None

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.prev is not None and node.val <= self.prev:
                return False

            self.prev = node.val

            return inorder(node.right)

        return inorder(root)
        