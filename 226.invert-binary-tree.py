#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # if not root:
        #     return None
        
        # queue = deque([root])

        # while queue:
        #     cur = queue.popleft()
        #     cur.left, cur.right = cur.right, cur.left

        #     if cur.left:
        #         queue.append(cur.left)
        #     if cur.right:
        #         queue.append(cur.right)
        
        # return root
# @lc code=end

