# Last updated: 5/12/2025, 12:08:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        # Find the middle element
        mid = len(nums) // 2
        
        # Create a new node with the middle element as the root
        root = TreeNode(nums[mid])
        
        # Recursively construct the left subtree
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively construct the right subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root