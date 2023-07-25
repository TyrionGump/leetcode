#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if str.isspace(s):
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:

            if not str.isalnum(s[left]):
                left += 1
            
            if not str.isalnum(s[right]):
                right -= 1
            
            if str.isalnum(s[left]) and str.isalnum(s[right]):
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
        return True
            

            
        
# @lc code=end

