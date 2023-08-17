/*
 * @lc app=leetcode id=219 lang=java
 *
 * [219] Contains Duplicate II
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> lastPosRecords = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (lastPosRecords.containsKey(nums[i])) {
                if (Math.abs(lastPosRecords.get(nums[i]) - i) <= k) {
                    return true;
                } else {
                    lastPosRecords.put(nums[i], i);
                }
            } else {
                lastPosRecords.put(nums[i], i);
            }
        }

        return false;
    }
}
// @lc code=end

