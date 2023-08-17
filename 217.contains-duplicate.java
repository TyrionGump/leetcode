/*
 * @lc app=leetcode id=217 lang=java
 *
 * [217] Contains Duplicate
 */

// @lc code=start

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> uniques = new HashSet<>();

        for (int n : nums) {
            if (uniques.contains(n)) {
                return true;
            }

            uniques.add(n);
        }

        return false;
    }
}
// @lc code=end

