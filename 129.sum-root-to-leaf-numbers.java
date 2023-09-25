/*
 * @lc app=leetcode id=129 lang=java
 *
 * [129] Sum Root to Leaf Numbers
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
    public int sumNumbers(TreeNode root) {
        return add(root, 0);
        
    }

    public int add(TreeNode currentNode, int currentSum) {

        if (currentNode == null) {
            return 0;
        }

        currentSum  = currentSum * 10 + currentNode.val;

        if (currentNode.left == null && currentNode.right == null) {
            return currentSum;
        }

        return add(currentNode.left, currentSum) + add(currentNode.right, currentSum);
    }
}
// @lc code=end

