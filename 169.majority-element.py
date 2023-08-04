#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore Vote Algorithm

        candicate = 0
        duplication_count = 0

        for num in nums:
            if duplication_count == 0:
                candicate = num
            
            if num == candicate:
                duplication_count += 1
            else:
                duplication_count -= 1
        
        return candicate
            
            
                
# @lc code=end

