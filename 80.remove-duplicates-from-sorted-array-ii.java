/*
 * @lc app=leetcode id=80 lang=java
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {

        int currentFillIdx = 2;

        for (int i = 2; i < nums.length; i++) {
            if (nums[i] > nums[currentFillIdx - 2]) {
                nums[currentFillIdx++] = nums[i];
            }
        }

        return currentFillIdx;
    }
}
// @lc code=end

