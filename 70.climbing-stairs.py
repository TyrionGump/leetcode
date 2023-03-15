#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        
        step1 = 1
        step2 = 2

        for i in range(3, n + 1):
            currentStep = step1 + step2
            step1 = step2
            step2 = currentStep 
        return step2
        
# @lc code=end

