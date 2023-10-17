#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:

        s_size = len(s)

        dp = [0 for _ in range(s_size + 1)]

        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, s_size + 1):
            if 0 < int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[s_size]
        
# @lc code=end

