#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
 
            
        
# @lc code=end

