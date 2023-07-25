#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        
        return max_profit
# @lc code=end

