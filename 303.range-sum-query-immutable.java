/*
 * @lc app=leetcode id=303 lang=java
 *
 * [303] Range Sum Query - Immutable
 */

// @lc code=start
class NumArray {

    private int[] sumAtEachElement;

    public NumArray(int[] nums) {
        sumAtEachElement = nums;

        for (int i = 1; i < sumAtEachElement.length; i++) {
            sumAtEachElement[i] += sumAtEachElement[i - 1];
        }
    }
    
    public int sumRange(int left, int right) {
        
        if (left == 0) {
            return sumAtEachElement[right];
        } else {
            return sumAtEachElement[right] - sumAtEachElement[left - 1];
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */
// @lc code=end

