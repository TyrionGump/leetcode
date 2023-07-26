/*
 * @lc app=leetcode id=136 lang=java
 *
 * [136] Single Number
 */

// @lc code=start

import java.util.Set;

class Solution {
    public int singleNumber(int[] nums) {
        int xor = 0;

        for(int num : nums) {
            xor = xor ^ num;
        }

        return xor;
        
    }
}
// @lc code=end

