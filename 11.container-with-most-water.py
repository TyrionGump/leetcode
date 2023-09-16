#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            max_area = max(max_area, (right - left) * min(height[right], height[left]))
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area
# @lc code=end

