#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n > 3:
            n /= 3
        
        if n == 3 or n == 1:
            return True
        else:
            return False
# @lc code=end

