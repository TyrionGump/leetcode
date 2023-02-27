#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        return cur
                
                


# @lc code=end
