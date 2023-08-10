/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        String res = "";

        for (int i = 0; i < s.length(); i++) {
            String tmp1 = this.expand(i, i, s);
            
            if (tmp1.length() > res.length()) {
                res = tmp1;
            }

            String tmp2 = this.expand(i, i + 1, s);

            if (tmp2.length() > res.length()) {
                res = tmp2;
            }
        }

        return res;

    }

    public String expand(int l, int r, String s) {
        while (l >= 0 && r <= s.length() - 1 && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }

        return s.substring(l + 1, r);
    }
}
// @lc code=end

