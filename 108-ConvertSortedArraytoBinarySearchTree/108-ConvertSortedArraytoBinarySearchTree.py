# Last updated: 5/12/2025, 12:07:43 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None

        def arrayToBST(left,right):

            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])  
            node.left = arrayToBST(left, mid - 1)  
            node.right = arrayToBST(mid + 1, right)  
            return node

        return arrayToBST(0,len(nums) - 1)
            

        


        