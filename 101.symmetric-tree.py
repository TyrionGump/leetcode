#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_left_right(root, root)
    
    def check_left_right(self, left, right):

        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return left.val == right.val and self.check_left_right(left.left, right.right) and self.check_left_right(left.right, right.left)
        

        
# @lc code=end

