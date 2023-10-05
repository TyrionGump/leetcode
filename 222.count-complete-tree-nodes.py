#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = 0
        tree_height = self.countHeight(root)

        while root:
            if self.countHeight(root.right) == tree_height - 1:
                res += 1 << tree_height
                root = root.right
            else:
                res += 1 << tree_height - 1
                root = root.left
            
            tree_height -= 1
        
        return res

    def countHeight(self, root):
        if not root:
            return -1
        else:
            return 1 + self.countHeight(root.left)
        
# @lc code=end

