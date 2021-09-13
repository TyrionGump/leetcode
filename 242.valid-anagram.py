#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # ss = list(s)
        # tt = list(t)

        # # sort() is faster than sorted()
        # ss.sort()
        # tt.sort()

        # return ss == tt
        
        dict1 = {}
        dict2 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for i in t:
            dict2[i] = dict2.get(i, 0) + 1 
        
        return dict1 == dict2
        
# @lc code=end

