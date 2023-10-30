#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]

# @lc code=end

