#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        left = columnNumber
        res = ""

        while left > 0:
            left, reminder = divmod(left - 1, 26)
            res = chr(65 + reminder) + res
        return res
                 
        
# @lc code=end

