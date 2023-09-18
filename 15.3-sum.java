/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 */

// @lc code=start

import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList();

        for (int i = 0; i < nums.length - 2; i++) {

            int target = -nums[i];
            int left = i + 1;
            int right = nums.length - 1;

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            while (left < right) {
                if (nums[left] + nums[right] < target) {
                    left++;
                } else if (nums[left] + nums[right] > target) {
                    right--;
                } else {
                    List<Integer> tempResult = List.of(nums[i], nums[left], nums[right]);
                    res.add(tempResult);

                    while (left < right && nums[left] == tempResult.get(1)) {
                        left++;
                    }

                    while (left < right && nums[right] == tempResult.get(2)) {
                        right--;
                    }
                }
            }
        }

        return res;
    }
}
// @lc code=end
