#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, val in enumerate(numbers):
            search_num = target - val
            # Do not use slice here. It is a O(n) operation.
            search_idx = self.binary_search(numbers, idx+1, len(numbers) - 1, search_num)
            
            if search_idx is not None:
                return [idx + 1, search_idx + 1]
        return None
            

    
    def binary_search(self, nums, left, right, target):
        l = left
        r = right
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        else:
            return None
        
# @lc code=end

