# Last updated: 5/7/2025, 2:03:40 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        def inorder(root):
            if root is None:
                return

            inorder(root.left)       
            sol.append(root.val)    
            inorder(root.right)      

        sol = []
        inorder(root)
        return sol