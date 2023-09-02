#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        root_idx_inorder = {}
        node_count = len(preorder)

        for idx, val in enumerate(inorder):
            root_idx_inorder[val] = idx
        
        return self.build(preorder, 0, node_count - 1, inorder, 0, node_count - 1, root_idx_inorder)
    
    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end, root_idx_inorder):
        
        if pre_start > pre_end or in_start > in_end:
            return None
        
        root = TreeNode(preorder[pre_start])
        root_idx = root_idx_inorder[root.val]
        num_left = root_idx - in_start

        root.left = self.build(preorder, pre_start + 1, pre_start + num_left, inorder, in_start, root_idx - 1, root_idx_inorder)
        root.right = self.build(preorder, pre_start + num_left + 1, pre_end, inorder, root_idx + 1, in_end, root_idx_inorder)

        return root

        



        
# @lc code=end

