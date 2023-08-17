#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        unique_nums = set()

        for n in nums:
            if n not in unique_nums:
                unique_nums.add(n)
            else:
                return True
        
        return False
# @lc code=end

