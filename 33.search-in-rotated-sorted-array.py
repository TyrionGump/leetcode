#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]

            if (nums[mid] < nums[0]) == (target < nums[0]):
                mid_val = nums[mid]
            
            else:
                if target < nums[0]:
                    mid_val = -float('inf')
                else:
                    mid_val = float('inf')
            
            if mid_val == target:
                return mid
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
            
# @lc code=end

