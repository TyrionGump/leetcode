#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        last_pos_record = {}

        for idx, n in enumerate(nums):
            if n in last_pos_record:
                if abs(last_pos_record[n] - idx) <= k:
                    return True
                else:
                    last_pos_record[n] = idx
            else:
                last_pos_record[n] = idx
        
        return False

        
# @lc code=end

