/*
 * @lc app=leetcode id=222 lang=java
 *
 * [222] Count Complete Tree Nodes
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
    public int countNodes(TreeNode root) {

        int res = 0;
        int treeHeight = countHeight(root);

        while (root != null) {
            if (countHeight(root.right) == treeHeight - 1) {
                res += 1 << treeHeight;
                root = root.right;
            } else {
                res += 1 << treeHeight - 1;
                root = root.left;
            }

            treeHeight--;
        }

        return res;
        
    }

    private int countHeight(TreeNode root) {
        
        if (root == null) {
            return -1;
        }

        return 1 + countHeight(root.left);
    }
}
// @lc code=end

