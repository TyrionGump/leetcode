#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        # mid >= l takes more running time and memory
        # mid = (l + r) // 2 written in the loop improves the memory usage
        # use elif target < nums[mid]: improve the memory usage but increase running time
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
# @lc code=end

