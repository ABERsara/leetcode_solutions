# Last updated: 5/11/2025, 5:04:08 PM
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [0] * len(nums)

        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1
        return -1