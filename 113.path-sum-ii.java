/*
 * @lc app=leetcode id=113 lang=java
 *
 * [113] Path Sum II
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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        return this.dfs(root, targetSum, 0, new ArrayList<>(), new ArrayList<>());
    }

    public List<List<Integer>> dfs(TreeNode root, int targetSum, int pathSum, List<List<Integer>> res, List<Integer> path) {
        
        if (root == null) {
            return res;
        }

        path.add(root.val);
        pathSum += root.val;

        if (pathSum == targetSum && root.left == null && root.right == null) {
            res.add(new ArrayList<>(path));
        }

        this.dfs(root.left, targetSum, pathSum, res, path);
        this.dfs(root.right, targetSum, pathSum, res, path);

        path.remove(path.size() - 1);
        
        return res;
    }
}
// @lc code=end

