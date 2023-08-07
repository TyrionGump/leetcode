#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res <<= 1
            res += n & 1
            n >>= 1
        return res

        
# @lc code=end

