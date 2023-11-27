#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums) - 1, 2):
            res += nums[i]
        
        return res
# @lc code=end

