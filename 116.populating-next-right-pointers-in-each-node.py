#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
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

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        
        level_start = root
        curr_node = None

        while level_start.left:
            curr_node = level_start

            while curr_node:
                curr_node.left.next = curr_node.right
                if curr_node.next:
                    curr_node.right.next = curr_node.next.left
                curr_node = curr_node.next
            
            level_start = level_start.left
        
        return root
        
# @lc code=end

