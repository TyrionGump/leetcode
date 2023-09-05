#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, 0, res, [])
        return res

    def dfs(self, root, targetSum, path_sum, res, path: list[int]):
        if not root:
            return
        
        path_sum += root.val
        path.append(root.val)
    
        if path_sum == targetSum and not root.left and not root.right:
            res.append(list(path))
        

        self.dfs(root.left, targetSum, path_sum, res, path)
        self.dfs(root.right, targetSum, path_sum, res, path)

        path.pop()

        
# @lc code=end

