/*
 * @lc app=leetcode id=16 lang=java
 *
 * [16] 3Sum Closest
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        Arrays.sort(nums);

        int numsSize = nums.length;

        int closetSum = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < numsSize - 2; i++) {

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = numsSize - 1;

            while (left < right) {

                int currentSum = nums[i] + nums[left] + nums[right];

                if (Math.abs(currentSum - target) < Math.abs(closetSum - target)) {
                    closetSum = currentSum;
                }

                if (currentSum == target) {
                    return currentSum;
                } else if (currentSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return closetSum;
    }
}
// @lc code=end

