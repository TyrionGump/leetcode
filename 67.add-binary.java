/*
 * @lc app=leetcode id=67 lang=java
 *
 * [67] Add Binary
 */

// @lc code=start
class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        StringBuilder res = new StringBuilder();

        while (i >= 0 || j >= 0 || carry > 0) {
            if (i >= 0) {
                carry += a.charAt(i) - '0';
                i--;
            }

            if (j >= 0) {
                carry += b.charAt(j) - '0';
                j--;
            }
            
            res.append(carry % 2);
            carry /= 2;
        }

        return res.reverse().toString();
    }
}
// @lc code=end

