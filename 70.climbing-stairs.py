#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # [0, 1, 2, 3, 5]
        # f(n) = f(n - 1) + f(n - 2) n > 2
        if n == 1:
            return n
        
        step1 = 1
        step2 = 2
        for _ in range(3, n + 1):
            currentStep = step1 + step2
            step1 = step2
            step2 = currentStep 
        return step2
        
        # Pure recursion will die since its duplicated calculation
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# @lc code=end

