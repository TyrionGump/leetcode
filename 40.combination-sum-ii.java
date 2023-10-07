/*
 * @lc app=leetcode id=40 lang=java
 *
 * [40] Combination Sum II
 */

// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        checkCombos(candidates, target, 0, target, new ArrayList<>(), res);
        return res;
    }

    private void checkCombos(int[] candidates, int target, int currentIdx, int remain, List<Integer> currentCombo, List<List<Integer>> res) {
        
        if (remain == 0) {
            res.add(new ArrayList<>(currentCombo));
            return;
        } else if (remain < 0) {
            return;
        }

        for (int i = currentIdx; i < candidates.length; i++) {
            if (i > currentIdx && candidates[i] == candidates[i - 1]) {
                continue;
            }

            currentCombo.add(candidates[i]);
            checkCombos(candidates, target, i + 1, remain - candidates[i], currentCombo, res);
            currentCombo.remove(currentCombo.size() - 1);
        }
    }
}
// @lc code=end

