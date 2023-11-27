/*
 * @lc app=leetcode id=643 lang=java
 *
 * [643] Maximum Average Subarray I
 */

// @lc code=start

import java.util.stream.Stream;

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int current_sum = 0;
        int max_sum = 0;

        for (int i = 0; i < k; i++) {
            current_sum += nums[i];
        }
        max_sum = current_sum;

        for (int i = k; i < nums.length; i++) {
            current_sum += nums[i] - nums[i - k];
            max_sum = Math.max(max_sum, current_sum);
        }

        return (double) max_sum / k;
    }
}
// @lc code=end

