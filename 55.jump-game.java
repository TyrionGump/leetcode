/*
 * @lc app=leetcode id=55 lang=java
 *
 * [55] Jump Game
 */

// @lc code=start
class Solution {
    public boolean canJump(int[] nums) {
        int curPos = 0;
        
        for (int i = 0; i <= curPos; i++) {
            curPos = Math.max(curPos, i + nums[i]);
            if (curPos >= nums.length - 1) {
                return true;
            }
        }

        return false;
    }
}
// @lc code=end

