#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current_fill_idx = 0

        for val in nums:
            if current_fill_idx < 2 or val > nums[current_fill_idx - 2]:
                nums[current_fill_idx] = val
                current_fill_idx += 1
        
        return current_fill_idx


            

        

# @lc code=end

