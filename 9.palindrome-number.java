/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversedX = 0;
        while (x > reversedX) {
            reversedX = reversedX * 10 + x % 10;
            x /= 10;
        }
        
        // even condition || odd condition
        return x == reversedX || x == (int) (reversedX / 10);
    }
}
// @lc code=end

