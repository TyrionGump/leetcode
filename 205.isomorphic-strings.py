#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Two dictionaries to store the mappings
        map_st = {}  # Mapping from s to t
        map_ts = {}  # Mapping from t to s

        for char_s, char_t in zip(s, t):
            if char_s in map_st:
                if map_st[char_s] != char_t:
                    return False
            else:
                map_st[char_s] = char_t

            if char_t in map_ts:
                if map_ts[char_t] != char_s:
                    return False
            else:
                map_ts[char_t] = char_s

        return True
        
# @lc code=end

