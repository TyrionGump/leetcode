#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l = 1
        r = x
        mid = 0
        while l <= r:
            mid = (l + r) // 2

            if x // mid == mid:
                return mid
            elif x // mid > mid:
                l = mid + 1
            else:
                r = mid - 1
        
        return r;
        
# @lc code=end

