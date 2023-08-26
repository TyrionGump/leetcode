#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if not n or n == 1:
            return n
        
        res = [0] * (n+1)
        res[0], res[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                res[i] += res[j-1] * res[i - j]
        return res[n]
        

# @lc code=end

