#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_list = []
        max_num = 0
        current_num = 0
        
        current_str = s
        for i in current_str:
            if i not in check_list:
                check_list.append(i)
                current_num += 1
            else:
                if current_num > max_num:
                    max_num = current_num
                repeat_idx = check_list.index(i)
                check_list = check_list[(repeat_idx + 1):]
                check_list.append(i)
                current_num = len(check_list)
                
        if current_num > max_num:
            max_num = current_num
        
        return max_num
# @lc code=end

