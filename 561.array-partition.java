/*
 * @lc app=leetcode id=561 lang=java
 *
 * [561] Array Partition
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);

        int res = 0;

        for (int i = 0; i < nums.length; i+=2) {
            res += nums[i];
        }

        return res;
    }
}
// @lc code=end

