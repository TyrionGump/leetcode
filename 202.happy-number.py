#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_digits(num):
            digits_sum = 0
            while num > 0:
                digits_sum += pow(num % 10, 2)
                num //= 10

            return digits_sum
         
        
        slow, quick = n, sum_digits(n)
        
        # If the quick pointer detects 1, end the loop in advance
        while quick != 1 and slow != quick:
            slow = sum_digits(slow)
            quick = sum_digits(sum_digits(quick))
        return quick == 1

        

# @lc code=end

