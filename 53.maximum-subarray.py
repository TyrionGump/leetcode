#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        max_sum = nums[0]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            max_sum = max(max_sum, dp[i])
        
        return max_sum
# @lc code=end

