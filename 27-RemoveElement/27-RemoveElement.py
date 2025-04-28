# Last updated: 4/28/2025, 2:21:53 PM
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        expected = [num for num in nums if num != val]
        for i in range(len(expected)):
            nums[i] = expected[i]
        
        return len(expected)
