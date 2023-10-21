#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrace(nums, 0, [], res)
        return res
    
    def backtrace(self, nums, current_idx, current_combos, res):
        
        res.append(current_combos[:])

        for i in range(current_idx, len(nums)):
            current_combos.append(nums[i])
            self.backtrace(nums, i + 1, current_combos, res)
            current_combos.pop()
# @lc code=end

