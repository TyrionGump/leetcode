/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxProfit = 0;

        while (right < prices.length) {
            if (prices[right] < prices[left]) {
                left = right;
            } else {
                maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
            }
            right++;
        }

        return maxProfit;
    }
}
// @lc code=end

