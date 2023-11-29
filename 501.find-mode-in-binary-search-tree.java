/*
 * @lc app=leetcode id=501 lang=java
 *
 * [501] Find Mode in Binary Search Tree
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
    int currentCount = 0;
    int maxCount = 0;
    List<Integer> modes = new ArrayList<>();
    int preInorderNodeVal = -1;

    public int[] findMode(TreeNode root) {
        inorder(root);
        int[] res = new int[this.modes.size()];
        for (int i = 0; i < res.length; i++) {
            res[i] = this.modes.get(i);
        }

        return res;
    }

    private void inorder(TreeNode root) {
        if (root == null) {
            return;
        }

        this.inorder(root.left);
        
        if (this.preInorderNodeVal == root.val) {
            this.currentCount++;
        } else {
            this.currentCount = 1;
        }

        if (this.currentCount == this.maxCount) {
            this.modes.add(root.val);
        } else if (this.currentCount > this.maxCount) {
            this.modes.clear();
            this.modes.add(root.val);
            this.maxCount = this.currentCount;
        }

        this.preInorderNodeVal = root.val;
        this.inorder(root.right);
    }
}
// @lc code=end

