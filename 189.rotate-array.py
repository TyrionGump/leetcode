#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        cut_idx = len(nums) - k
        left = nums[:cut_idx]
        right = nums[cut_idx:]
        # nums = right + left notice that nums should be modified in-place
        nums[:] = right + left

             
            
        
# @lc code=end

