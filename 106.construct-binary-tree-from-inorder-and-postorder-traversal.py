#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
        self.inorder = None
        self.postorder = None
        self.root_val2idx_inorder = None

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        tree_size = len(inorder)
        self.root_val2idx_inorder = dict(zip(inorder, range(tree_size)))
        self.inorder = inorder
        self.postorder = postorder

        return self.build(0, tree_size - 1, tree_size - 1)
    

    def build(self, inorder_start, inorder_end, postorder_end):
        
        if (inorder_start > inorder_end):
            return None
        
        root = TreeNode(self.postorder[postorder_end])
        root_idx_inorder = self.root_val2idx_inorder[root.val]
        right_tree_size = inorder_end - root_idx_inorder
        
        root.left = self.build(inorder_start, root_idx_inorder - 1, postorder_end - right_tree_size - 1)
        root.right = self.build(root_idx_inorder + 1, inorder_end, postorder_end - 1)
        
        return root

# @lc code=end

