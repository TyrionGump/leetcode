/*
 * @lc app=leetcode id=91 lang=java
 *
 * [91] Decode Ways
 */

// @lc code=start
class Solution {
    public int numDecodings(String s) {
        int strLength = s.length();

        int[] dp = new int[strLength + 1];

        dp[0] = 1;
        dp[1] = s.charAt(0) == '0' ? 0 : 1;

        for (int i = 2; i < strLength + 1; i++) {
            
            int oneStep = Integer.valueOf(s.substring(i - 1, i));
            int twoStep = Integer.valueOf(s.substring(i - 2, i));

            if (oneStep >= 1 && oneStep <= 9) {
                dp[i] += dp[i - 1];
            }

            if (twoStep >= 10 && twoStep <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[strLength];
    }
}
// @lc code=end

