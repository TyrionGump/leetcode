/*
 * @lc app=leetcode id=674 lang=java
 *
 * [674] Longest Continuous Increasing Subsequence
 */

// @lc code=start
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int maxSequenceLength = 1;
        int currSequenceLength = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                currSequenceLength++;
            } else {
                maxSequenceLength = Math.max(maxSequenceLength, currSequenceLength);
                currSequenceLength = 1;
            }
        }

        return Math.max(maxSequenceLength, currSequenceLength);
    }
}
// @lc code=end

