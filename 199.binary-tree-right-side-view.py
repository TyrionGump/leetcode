#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []
        level_nodes = deque([root])

        while level_nodes:
            level_size = len(level_nodes)
            for _ in range(level_size):
                curr_node = level_nodes.popleft()
                
                if curr_node.left:
                    level_nodes.append(curr_node.left)
                if curr_node.right:
                    level_nodes.append(curr_node.right)
                
            res.append(curr_node.val)
        
        return res
                
            
            
            

            
# @lc code=end

