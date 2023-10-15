#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cur_pos = 0
        next_pos = 0

        for i in range(len(nums)):
            if i > cur_pos:
                return False
            next_pos = max(next_pos, i + nums[i])
            if next_pos >= len(nums) - 1:
                return True
            cur_pos = next_pos

        return True if cur_pos >= len(nums) - 1 else False
        
# @lc code=end

