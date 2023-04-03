/*
 * @lc app=leetcode id=111 lang=java
 *
 * [111] Minimum Depth of Binary Tree
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
    public int minDepth(TreeNode root) {

        if (root == null) {
            return 0;
        } else if (root.left == null && root.right == null) {
            return 1;
        }

        int leftHeight = this.minDepth(root.left);
        int rightHeight = this.minDepth(root.right);

        if (root.left == null) {
            return rightHeight + 1;
        } else if (root.right == null) {
            return leftHeight + 1;
        }

        return Math.min(leftHeight, rightHeight) + 1;
        
    }
}
// @lc code=end

