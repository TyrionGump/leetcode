#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        curr_level = 0

        while queue:
            level_res = []
            level_size = len(queue)

            for _ in range(level_size):
                if curr_level % 2 == 0:
                    curr_node = queue.pop()
                    if curr_node.left:
                        queue.appendleft(curr_node.left)
                    if curr_node.right:
                        queue.appendleft(curr_node.right)

                else:
                    curr_node = queue.popleft()
                    if curr_node.right:
                        queue.append(curr_node.right)
                    if curr_node.left:
                        queue.append(curr_node.left)
            
                level_res.append(curr_node.val)
        
            res.append(level_res)
            curr_level += 1
        
        return res
             
        
# @lc code=end

