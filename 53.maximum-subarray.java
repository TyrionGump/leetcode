/*
 * @lc app=leetcode id=53 lang=java
 *
 * [53] Maximum Subarray
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        int curr_sum = nums[0];
        int curr_max = nums[0];

        for (int i = 1; i < nums.length; i++) {
            curr_sum = curr_sum + nums[i] > nums[i] ? curr_sum + nums[i] : nums[i];
            curr_max = Math.max(curr_max, curr_sum);
        }

        return curr_max;
    }
}
// @lc code=end

