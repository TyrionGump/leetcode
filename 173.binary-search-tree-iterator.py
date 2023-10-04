#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.pushAllSubTree(root)
        
    def next(self) -> int:
        if self.hasNext():
            cur_node = self.stack.pop()
            if cur_node.right:
                self.pushAllSubTree(cur_node.right)
            return cur_node.val
        else:
            return -1

    def hasNext(self) -> bool:
        return self.stack
    
    def pushAllSubTree(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

