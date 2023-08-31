#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            level_res = []
            curr_level_size = len(queue)

            for i in range(curr_level_size):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                level_res.append(curr_node.val)
            
            res.append(level_res)
        
        return res

                


    
        
# @lc code=end

