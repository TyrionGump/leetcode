#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        
        # original_x = x
        # reversed_num_sum = 0
        # while(x > 0):
        #     reversed_num_sum = x % 10 + reversed_num_sum * 10
        #     x = x // 10
        
        # if (reversed_num_sum == original_x):
        #     return True
        # else:
        #     return False

        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        return x == reversed_x or x == int(reversed_x / 10)

        
# @lc code=end

