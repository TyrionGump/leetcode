#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_dest = 0
        next_dest = 0
        

        for i in range(len(nums) - 1):
            next_dest = max(next_dest, nums[i] + i)

            if i == cur_dest:
                cur_dest = next_dest
                jumps += 1
        
        return jumps

        
# @lc code=end

