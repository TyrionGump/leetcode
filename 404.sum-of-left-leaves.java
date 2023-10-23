/*
 * @lc app=leetcode id=404 lang=java
 *
 * [404] Sum of Left Leaves
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
    public int sumOfLeftLeaves(TreeNode root) {
        return sumLeft(root, false);
    }

    public int sumLeft(TreeNode root, boolean isLeft) {
        if (root == null) {
            return 0;
        }

        if (isLeft && root.left == null && root.right == null) {
            return root.val;
        }
        return sumLeft(root.left, true) + sumLeft(root.right, false);
    }
}
// @lc code=end

