#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        left, right = 0, len(nums) - 1

        # Search for the starting position
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res[0] = mid
                right = mid - 1  # Continue searching on the left side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If we didn't find the target at all, return [-1, -1]
        if res[0] == -1:
            return res

        # Start the second loop from the found start position
        left, right = res[0], len(nums) - 1
        # Search for the ending position
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res[1] = mid
                left = mid + 1  # Continue searching on the right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res


# @lc code=end

