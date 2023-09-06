/*
 * @lc app=leetcode id=114 lang=java
 *
 * [114] Flatten Binary Tree to Linked List
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
    private TreeNode prevNode;
    public void flatten(TreeNode root) {
        
        if (root == null) {
            return;
        }

        this.flatten(root.right);
        this.flatten(root.left);

        root.left = null;
        root.right = prevNode;
        prevNode = root;
    }
}
// @lc code=end

