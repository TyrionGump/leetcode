/*
 * @lc app=leetcode id=485 lang=java
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxConsecutives = 0;
        int currentConsecutives = 0;

        for (int val : nums) {
            if (val == 0) {
                maxConsecutives = Math.max(maxConsecutives, currentConsecutives);
                currentConsecutives = 0;
            } else {
                currentConsecutives++;
            }
        }

        return Math.max(currentConsecutives, maxConsecutives);
    }
}
// @lc code=end

