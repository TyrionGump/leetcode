#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # value_idx = {}
        # for idx, n in enumerate(nums):
        #     sub_res = target - n
        #     if sub_res in value_idx:
        #         return [value_idx[sub_res], idx]
        #     else:
        #         value_idx[n] = idx
        nums_idx = [(val, idx) for idx, val in enumerate(nums)]
        nums_idx.sort(key=lambda x:x[0])

        for i in range(len(nums_idx)):
            search_num = target - nums_idx[i][0]
            # Do not use slice here. It is a O(n) operation.
            search_idx = self.binary_search(nums_idx, i+1, len(nums_idx) - 1, search_num)
            
            if search_idx is not None:
                return [nums_idx[i][1], nums_idx[search_idx][1]]
        return None
            

    
    def binary_search(self, nums, left, right, target):
        l = left
        r = right
        while l <= r:
            mid = (l + r) // 2
            if nums[mid][0] == target:
                return mid
            elif nums[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        else:
            return None

        
# @lc code=end

