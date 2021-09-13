#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        self.quick_sort(nums, left, right)
        return nums
    
    def quick_sort(self, nums, left, right):
        if left < right:
            mid = self.partition(nums, left, right)
            self.quick_sort(nums, left, mid - 1)
            self.quick_sort(nums, mid + 1, right)


    def partition(self, nums, left, right):
        tmp = nums[left]
        while left < right:
            while left < right and nums[right] >= tmp:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= tmp:
                left += 1
            nums[right] = nums[left]
        
        nums[left] = tmp
        return left
    
    


        
# @lc code=end

