#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from email.policy import default


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        cur = 1
        for i in range(1, len(nums)):
            if (nums[i] != nums[i-1]):
                nums[cur] = nums[i]
                cur += 1
        
        return cur
            
            

        
# @lc code=end

