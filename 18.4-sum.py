#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        nums_size = len(nums)
        res = []

        for i in range(nums_size - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, nums_size - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = nums_size - 1

                while left < right:

                    curr_res = nums[i] + nums[j] + nums[left] + nums[right] - target

                    if curr_res == 0:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1 
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif curr_res < 0:
                        left += 1
                    else:
                        right -= 1
        
        return res

            

        
        
        
# @lc code=end

