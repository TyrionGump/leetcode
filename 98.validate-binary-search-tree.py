#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def is_valid(tree, min_val, max_val):
            if not tree:
                return True
            if (min_val is not None and tree.val <= min_val) or (max_val is not None and tree.val >= max_val):
                return False
            return is_valid(tree.left, min_val, tree.val) and is_valid(tree.right, tree.val, max_val)
        return is_valid(root, None, None)
        

        
# @lc code=end

