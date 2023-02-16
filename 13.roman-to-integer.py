#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        cur = 0
        res = 0
        symbol_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sub_map = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
        # sub_map2 = {"I": {"V", "X"}, "X": {"L", "C"}, "C": ["D", "M"]}

        while cur < len(s):
            if cur + 1 < len(s) and s[cur] in sub_map.keys() and s[cur + 1] in sub_map.get(s[cur]):
                res += symbol_to_val.get(s[cur + 1]) - symbol_to_val.get(s[cur])
                cur += 2
            else:
                res += symbol_to_val.get(s[cur])
                cur += 1 
        
        return res

                
                
        
# @lc code=end

