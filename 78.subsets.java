/*
 * @lc app=leetcode id=78 lang=java
 *
 * [78] Subsets
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backTracing(nums, 0, new ArrayList<>(), res);
        return res;
    }

    private void backTracing(int[] nums, int currentIdx, List<Integer> currentCombo, List<List<Integer>> res) {
        res.add(new ArrayList<>(currentCombo));

        for (int i = currentIdx; i < nums.length; i++) {
            currentCombo.add(nums[i]);
            backTracing(nums, i + 1, currentCombo, res);
            currentCombo.remove(currentCombo.size() - 1);
        }
    }
}
// @lc code=end

