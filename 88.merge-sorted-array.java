/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int l = m - 1;
        int r = n - 1;

        while (l >= 0 && r >= 0) {
            if (nums1[l] > nums2[r]) {
                nums1[l + r + 1] = nums1[l];
                l--;
            } else {
                nums1[l + r + 1] = nums2[r];
                r--;
            }
        }
        
        for (int i = 0; i <= r; i++) {
            nums1[i] = nums2[i];
        }
    }
}
// @lc code=end

