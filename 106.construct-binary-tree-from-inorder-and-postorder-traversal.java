/*
 * @lc app=leetcode id=106 lang=java
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int[] inorder;
    private int[] postorder;
    private Map<Integer, Integer> rootToIdxInorder;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.inorder = inorder;
        this.postorder = postorder;
        int treeSize = inorder.length;
        this.rootToIdxInorder = new HashMap<>(treeSize);

        for (int i = 0; i < treeSize; i++) {
            this.rootToIdxInorder.put(inorder[i], i);
        }

        return this.build(0, treeSize - 1, treeSize - 1);
    }

    public TreeNode build(int inStart, int inEnd, int postEnd) {
        if (inStart > inEnd) {
            return null;
        }

        TreeNode root = new TreeNode(postorder[postEnd]);
        int rootIdx = rootToIdxInorder.get(root.val);
        int rightTreeSize = inEnd - rootIdx;

        root.left = this.build(inStart, rootIdx - 1, postEnd - rightTreeSize - 1);
        root.right = this.build(rootIdx + 1, inEnd, postEnd - 1);

        return root;
    }
}
// @lc code=end

