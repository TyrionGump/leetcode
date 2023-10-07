#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.checkCombos(candidates, target, 0, 0, [], res)
        return res

    def checkCombos(self, candidates, target, current_idx, current_sum, current_combo, res):
        if current_sum == target:
            res.append(current_combo[:])
            return
        elif current_sum > target:
            return
        
        for i in range(current_idx, len(candidates)):
            if i > current_idx and candidates[i] == candidates[i - 1]:
                continue
            current_combo.append(candidates[i])
            current_sum += candidates[i]
            
            self.checkCombos(candidates, target, i + 1, current_sum, current_combo, res)
            current_combo.pop()
            current_sum -= candidates[i]
        return
        
# @lc code=end

