#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, root, res):
        if root:
            self.traversal(root.left, res)
            self.traversal(root.right, res)
            res.append(root.val)
            
        
# @lc code=end

