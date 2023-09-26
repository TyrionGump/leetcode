/*
 * @lc app=leetcode id=18 lang=java
 *
 * [18] 4Sum
 */

// @lc code=start
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList();
        int numsSize = nums.length;
        
        for (int i = 0; i < numsSize - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            for (int j = i + 1; j < numsSize - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                int left = j + 1;
                int right = numsSize - 1;

                while (left < right) {

                    long currentRes = (long) nums[i] + (long) nums[j] + (long) nums[left] + (long) nums[right] - (long) target;

                    if (currentRes == 0) {
                        res.add(List.of(nums[i], nums[j], nums[left], nums[right]));

                        left++;
                        right--;
                        while (left < right && nums[left] == nums[left - 1]) {
                            left++;
                        }

                        while (left < right && nums[right] == nums[right + 1]) {
                            right--;
                        }
                    } else if (currentRes > 0) {
                        right--;
                    } else {
                        left++;
                    }
                }
            }
        }

        return res;

    }
}
// @lc code=end

