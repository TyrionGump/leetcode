#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        cur_level_nodes = deque()
        cur_level_nodes.append(root)

        while cur_level_nodes:
            cur_level_size = len(cur_level_nodes)
            prev_node = None

            for _ in range(cur_level_size):

                cur_node = cur_level_nodes.popleft()

                if prev_node:
                    prev_node.next = cur_node
            
                if cur_node.left:
                    cur_level_nodes.append(cur_node.left)
                if cur_node.right:
                    cur_level_nodes.append(cur_node.right)
                
                prev_node = cur_node
        
        return root
            
        
            

        
        
# @lc code=end

