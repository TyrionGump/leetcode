#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First idea
        # non_zeros = [val for val in nums if val]
        # nums[:len(non_zeros)] = non_zeros
        # nums[len(non_zeros):] = [0] * (len(nums) - len(non_zeros))

        # Second idea: swap
        zero_seeker = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[zero_seeker] == 0:
                nums[i], nums[zero_seeker] = nums[zero_seeker], nums[i]
            if nums[zero_seeker] != 0:
                zero_seeker += 1


        
# @lc code=end

