#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        expected_total = (1 + max_num) * max_num // 2

        for val in nums:
            expected_total -= val
        return expected_total
# @lc code=end

