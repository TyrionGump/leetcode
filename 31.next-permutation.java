/*
 * @lc app=leetcode id=31 lang=java
 *
 * [31] Next Permutation
 */

// @lc code=start
class Solution {
    public void nextPermutation(int[] nums) {
        
        int i = nums.length - 1;
        int j = nums.length - 1;

        while (i > 0 && nums[i - 1] >= nums[i]) {
            i--;
        }

        if (i == 0) {
            reverse(nums, 0, nums.length - 1);
            return;
        }

        int k = i - 1;
        while (nums[j] <= nums[k]) {
            j--;
        }
        swap(nums, k, j);
        
        reverse(nums, k + 1, nums.length - 1);

    
    }

    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
}
// @lc code=end

