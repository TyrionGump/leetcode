#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum(root, 0)

    def sum(self, curr_node, curr_sum):
        if not curr_node:
            return 0
        
        curr_sum = curr_sum * 10 + curr_node.val
        
        if not curr_node.left and not curr_node.right:
            return curr_sum
        
        return self.sum(curr_node.left, curr_sum) + self.sum(curr_node.right, curr_sum)

        
# @lc code=end

