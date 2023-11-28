#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr_sequence_length = 1
        max_sequence_length = 1

        for i in range(1, len(nums)):
            
            if nums[i] > nums[i - 1]:
                curr_sequence_length += 1
            else:
                max_sequence_length = max(max_sequence_length, curr_sequence_length)
                curr_sequence_length = 1
        
        return max(max_sequence_length, curr_sequence_length)
                
# @lc code=end

