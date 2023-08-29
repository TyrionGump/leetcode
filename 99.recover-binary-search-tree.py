#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.first_mistake_node = None
        self.second_mistake_node = None
        self.prev_node = TreeNode(-float("inf"))

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder_traversal(tree):
            if not tree:
                return

            inorder_traversal(tree.left)
            
            if not self.first_mistake_node and self.prev_node.val >= tree.val:
                self.first_mistake_node = self.prev_node
            
            if self.first_mistake_node and self.prev_node.val >= tree.val:
                self.second_mistake_node = tree
            
            self.prev_node = tree

            inorder_traversal(tree.right)
        
        inorder_traversal(root)

        temp = self.first_mistake_node.val
        self.first_mistake_node.val = self.second_mistake_node.val
        self.second_mistake_node.val = temp
   
# @lc code=end

