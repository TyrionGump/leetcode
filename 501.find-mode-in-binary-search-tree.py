#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
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
        self.modes = []  # Elements with the highest occurrence
        self.current_count = 0
        self.max_count = 0
        self.prev_val = None

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.modes
    
    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        if self.prev_val == root.val:
            self.current_count += 1
        else:
            self.current_count = 1

        if self.current_count == self.max_count:
            self.modes.append(root.val)
        elif self.current_count > self.max_count:
            self.modes = [root.val]
            self.max_count = self.current_count

        self.prev_val = root.val

        self.inorder(root.right)

        
# @lc code=end

