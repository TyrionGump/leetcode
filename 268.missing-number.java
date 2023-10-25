/*
 * @lc app=leetcode id=268 lang=java
 *
 * [268] Missing Number
 */

// @lc code=start
class Solution {
    public int missingNumber(int[] nums) {
        int maxNum = nums.length;
        int leftSum = (1 + maxNum) * maxNum / 2;

        for (int val : nums) {
            leftSum -= val;
        }

        return leftSum;
    }
}
// @lc code=end

