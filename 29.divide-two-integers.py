#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = +1 if dividend ^ divisor >= 0 else -1
        
        dividend, divisor = abs(dividend), abs(divisor)

        ans = 0      
        
        for power in range(31, -1, -1) :
            if pow(divisor, power) <= dividend:
                ans += (1 << power)
                dividend -= (divisor << power)
           
        ans = ans * sign
        
        if not (-2**31 <= ans <= 2**31-1):
            return 2**31 - 1
        else:
            return ans
        
   
# @lc code=end