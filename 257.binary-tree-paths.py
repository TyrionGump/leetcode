#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []
        self.dfs(root, res, "")
        return res
    
    
    def dfs(self, root, res, path):
        if not root:
            return
        if not root.left and not root.right:
            path += str(root.val)
            res.append(path)
            return
        
        path += "{}->".format(root.val)
        self.dfs(root.left, res, path)
        self.dfs(root.right, res, path)



        

        
# @lc code=end

