#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_consecutives = 0
        current_consecutives = 0

        for val in nums:
            if val == 0:
                max_consecutives = max(max_consecutives, current_consecutives)
                current_consecutives = 0
            else:
                current_consecutives += 1
        
        return max(max_consecutives, current_consecutives)
        
# @lc code=end

