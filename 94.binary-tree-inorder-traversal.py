#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
    
    # def in_order(self, tree_node):
    #     if tree_node:
    #         self.in_order(tree_node.left)
    #         self.res.append(tree_node.val)
    #         self.in_order(tree_node.right)
        

        

# @lc code=end

