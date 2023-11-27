#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        nums_size = len(nums)
        left = 0
        right = nums_size - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right += 1
            elif (nums[left] < nums[mid]):
                if nums[left] < target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False

# @lc code=end

