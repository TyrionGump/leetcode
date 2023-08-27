/*
 * @lc app=leetcode id=98 lang=java
 *
 * [98] Validate Binary Search Tree
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
    public boolean isValidBST(TreeNode root) {
        return isValid(root, null, null);
        
    }

    public boolean isValid(TreeNode root, Integer max, Integer min) {
        if (root == null) {
            return true;
        }

        if ((max != null && root.val >= max) || (min != null && root.val <= min)) {
            return false;
        }

        return isValid(root.left, root.val, min) && isValid(root.right, max, root.val);
    }
}
// @lc code=end

