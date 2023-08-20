#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while (n >= 1):
            if n == 2 or n == 1:
                return True
            else:
                n /= 2

        return False
        
# @lc code=end

