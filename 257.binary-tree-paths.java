/*
 * @lc app=leetcode id=257 lang=java
 *
 * [257] Binary Tree Paths
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        dfs(root, res, "");
        return res;
    }

    public void dfs(TreeNode root, List<String> res, String path) {
        if (root == null) {
            return;
        }

        if (root.left == null && root.right == null) {
            path += root.val;
            res.add(path);
            return;
        }


        path += root.val + "->";
        dfs(root.left, res, path);
        dfs(root.right, res, path);
    }
}
// @lc code=end

