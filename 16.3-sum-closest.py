#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = nums[0] + nums[1] + nums[2]

        for i in range (len(nums) - 2):
            if nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == target:
                    return curr_sum
                elif abs(curr_sum - target) < abs(res - target):
                    res = curr_sum
                
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
            
        return res


        
        

        
# @lc code=end

