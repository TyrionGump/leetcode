/*
 * @lc app=leetcode id=169 lang=java
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int duplicationCount = 0;

        for (int num : nums) {
            if (duplicationCount == 0) {
                candidate = num;
            }

            if (num == candidate) {
                duplicationCount++;
            } else {
                duplicationCount--;
            }
        }

        return candidate;
    }
}
// @lc code=end

