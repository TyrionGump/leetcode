#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = -float('inf')
        second_max = -float('inf')
        third_max = -float('inf')

        for val in nums:
            if val == first_max or val == second_max or val == third_max:
                continue

            if val > first_max:
                third_max = second_max
                second_max = first_max
                first_max = val

            elif val > second_max:
                third_max = second_max
                second_max = val

            elif val > third_max:
                third_max = val

        
        if third_max != -float('inf'):
            return third_max
        else:
            return first_max

        
# @lc code=end

