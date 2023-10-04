/*
 * @lc app=leetcode id=39 lang=java
 *
 * [39] Combination Sum
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        checkCombinations(candidates, target, 0, 0, new ArrayList<>(), res);
        return res;
    }

    private void checkCombinations(int[] candidates, int target, int currentIdx, int currentSum, List<Integer> currentCombo, List<List<Integer>> res) {
        
        if (currentSum == target) {
            res.add(new ArrayList<>(currentCombo));
        }

        for (int i = currentIdx; i < candidates.length; i++) {
            if (currentSum + candidates[i] > target) {
                continue;
            }
            currentCombo.add(candidates[i]);
            currentSum += candidates[i];
            checkCombinations(candidates, target, i, currentSum, currentCombo, res);
            currentCombo.remove(currentCombo.size() - 1);
            currentSum -= candidates[i];
        }
    }
}
// @lc code=end

