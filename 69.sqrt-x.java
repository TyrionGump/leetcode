/*
 * @lc app=leetcode id=69 lang=java
 *
 * [69] Sqrt(x)
 */

// @lc code=start
class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        int l = 1, r = x;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (mid == x / mid) {
                return mid;
            } else if (mid > x / mid) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }
    
}
// @lc code=end

