#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        trees_track = {}
        
        def generateTree(left, right):
            if (left, right) in trees_track:
                return trees_track[(left, right)]
            
            trees = []

            if (left > right):
                trees.append(None)
                return trees
            
            for root_val in range(left, right + 1):
                left_trees = generateTree(left, root_val - 1)
                right_trees = generateTree(root_val + 1, right)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)
            
            trees_track[(left, right)] = trees

            return trees
        
        return generateTree(1, n)
# @lc code=end

