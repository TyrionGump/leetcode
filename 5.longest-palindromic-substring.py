#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        for i in range(len(s)):
            tmp1 = expand(i, i)
            tmp2 = expand(i, i + 1)

            

            if len(tmp1) > len(res):
                res = tmp1
            
            if len(tmp2) > len(res):
                res = tmp2
            
        return res
# @lc code=end

