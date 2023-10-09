/*
 * @lc app=leetcode id=45 lang=java
 *
 * [45] Jump Game II
 */

// @lc code=start
class Solution {
    public int jump(int[] nums) {
        int jumps = 0;
        int currentEnd = 0;
        int nextEnd = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            nextEnd = Math.max(nextEnd, nums[i] + i);

            if (i == currentEnd) {
                currentEnd = nextEnd;
                jumps++;
            }
        }

        return jumps;
    }
}
// @lc code=end

