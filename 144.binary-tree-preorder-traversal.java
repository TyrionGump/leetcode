/*
 * @lc app=leetcode id=144 lang=java
 *
 * [144] Binary Tree Preorder Traversal
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
    // public List<Integer> preorderTraversal(TreeNode root) {
    //     // This method uses too much mem due to new list creation
    //     List<Integer> res = new ArrayList<>();
        
    //     if (root != null) {
    //         res.add(root.val);
    //         res.addAll(this.preorderTraversal(root.left));
    //         res.addAll(this.preorderTraversal(root.right));
    //         return res;
    //     } else {
    //         return List.of();
    //     }
    // }


    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        
        this.traversal(root, res);
        return res;
    }

    public void traversal(TreeNode root, List<Integer> res) {
        if (root != null) {
            res.add(root.val);
            traversal(root.left, res);
            traversal(root.right, res);
        }
    }
}
// @lc code=end

