#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size = len(needle)
        haystack_size = len(haystack)

        if needle_size > haystack_size:
            return -1

        for i in range(haystack_size):
            if haystack[i] == needle[0]:
                haystack_pointer = i
                needle_pointer = 0
                while needle_pointer < needle_size and haystack_pointer < haystack_size:
                    if haystack[haystack_pointer] == needle[needle_pointer]:
                        haystack_pointer += 1
                        needle_pointer += 1
                    else:
                        break
                
                if needle_pointer == needle_size:
                    return haystack_pointer - needle_size
                
        return -1
# @lc code=end

