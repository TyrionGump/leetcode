#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.checkCombination(candidates, target, 0, 0, [], res)
        return res

    def checkCombination(self, candidates, target, curr_idx, curr_sum, curr_combo, res):
        if (curr_sum > target):
            return
        elif (curr_sum == target):
            res.append(curr_combo[:])
            return
        
        for i in range(curr_idx, len(candidates)):
            curr_combo.append(candidates[i])
            curr_sum += candidates[i]
            self.checkCombination(candidates, target, i, curr_sum, curr_combo, res)
            curr_combo.pop()
            curr_sum -= candidates[i]
        
# @lc code=end

