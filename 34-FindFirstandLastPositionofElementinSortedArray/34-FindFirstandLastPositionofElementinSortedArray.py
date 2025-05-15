# Last updated: 5/15/2025, 1:58:42 PM
class Solution(object):
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid
                    right = mid - 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid
                    left = mid + 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx

        return [findFirst(nums, target), findLast(nums, target)]
