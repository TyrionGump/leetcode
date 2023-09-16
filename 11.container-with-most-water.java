/*
 * @lc app=leetcode id=11 lang=java
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        
        int left = 0;
        int right = height.length - 1;
        int maxAreaValue = 0;

        while (left < right) {

            maxAreaValue = Math.max(maxAreaValue, (right - left) * Math.min(height[left], height[right]));

            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }

        return maxAreaValue;
    }
}
// @lc code=end

