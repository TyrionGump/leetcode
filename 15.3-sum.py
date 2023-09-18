#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        i = 0

        while i < len(nums):
            
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    temp_res = [nums[i], nums[left], nums[right]]
                    res.append(temp_res)

                    while left < right and nums[left] == temp_res[1]:
                        left += 1
                    while left < right and nums[right] == temp_res[2]:
                        right -= 1
            
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            i += 1
        
        return res

        
# @lc code=end

