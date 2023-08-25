/*
 * @lc app=leetcode id=95 lang=java
 *
 * [95] Unique Binary Search Trees II
 */

// @lc code=start

import java.util.ArrayList;
import java.util.HashMap;

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
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) {
            return List.of();
        }
        Map<Pair, List<TreeNode>> treesTrack = new HashMap<>();
        return generateSubTreesMap(treesTrack, 1, n);
    }

    public List<TreeNode> generateSubTreesMap(Map<Pair, List<TreeNode>> treesTrack, int left, int right) {
        // Two pairs are considered as equal when both objects are equal. 
        // Here left and right are int. That should be fine.
        Pair range = new Pair<>(left, right);
        if (treesTrack.containsKey(range)) {
            return treesTrack.get(range);
        }

        List<TreeNode> trees = new ArrayList<>();
        if (left > right) {
            trees.add(null);
            return trees;
        }

        for(int root_val = left; root_val <= right; root_val++) {
            List<TreeNode> leftTrees = this.generateSubTreesMap(treesTrack, left, root_val - 1);
            List<TreeNode> rightTrees = this.generateSubTreesMap(treesTrack, root_val + 1, right);

            for(TreeNode leftTree : leftTrees) {
                for (TreeNode rightTree : rightTrees) {
                    trees.add(new TreeNode(root_val, leftTree, rightTree));
                }
            }
        }

        treesTrack.put(range, trees);
        return trees;
    }
}
// @lc code=end

