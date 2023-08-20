#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        
        res = []
        range_start_idx = 0

        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                if range_start_idx == i:
                  res.append('{}'.format(nums[i]))
                else:
                  res.append('{}->{}'.format(nums[range_start_idx], nums[i]))
                range_start_idx = i + 1
        
        if range_start_idx == len(nums) - 1:
            res.append("{}".format(nums[range_start_idx]))
        else:
            res.append('{}->{}'.format(nums[range_start_idx], nums[-1]))


        return res

                
                
# @lc code=end

