/*
 * @lc app=leetcode id=99 lang=java
 *
 * [99] Recover Binary Search Tree
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
    TreeNode firstMistake;
    TreeNode secondMistake;
    TreeNode previousNode = new TreeNode(Integer.MIN_VALUE);

    public void recoverTree(TreeNode root) {
        inOrderTraversal(root);

        int temp = this.firstMistake.val;
        this.firstMistake.val = this.secondMistake.val;
        this.secondMistake.val = temp;
    }

    public void inOrderTraversal(TreeNode root) {
        
        if (root == null) {
            return;
        }

        inOrderTraversal(root.left);

        if (this.firstMistake == null && this.previousNode.val > root.val) {
            this.firstMistake = this.previousNode;
        }

        if (this.firstMistake != null && this.previousNode.val > root.val) {
            this.secondMistake = root;
        }

        this.previousNode = root;

        inOrderTraversal(root.right);
    }
}
// @lc code=end

