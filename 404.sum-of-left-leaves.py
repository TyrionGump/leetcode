#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        return self.sum_left(root, False)

    def sum_left(self, root, is_left) -> int:
        if not root:
            return 0
        if not root.left and not root.right and is_left:  # Check if it's a left leaf node
            return root.val
        return self.sum_left(root.left, True) + self.sum_left(root.right, False)
        
        
# @lc code=end

