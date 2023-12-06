#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        while n > 1 and n % 4 == 0:
            n /= 4
        
        return n == 1
# @lc code=end

