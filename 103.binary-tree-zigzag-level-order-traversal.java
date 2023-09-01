/*
 * @lc app=leetcode id=103 lang=java
 *
 * [103] Binary Tree Zigzag Level Order Traversal
 */

// @lc code=start

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) {
            return List.of();
        }

        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root);
        List<List<Integer>> res = new ArrayList<>();
        int currentLevel = 0;

        while (!deque.isEmpty()) {
            int levelSize = deque.size();
            List<Integer> levelRes = new ArrayList<>(levelSize);
            TreeNode currentNode = null;

            for (int i = 0; i < levelSize; i++) {
                if (currentLevel % 2 == 0) {
                    currentNode = deque.pollLast();

                    if (currentNode.left != null) {
                        deque.addFirst(currentNode.left);
                    }
                    if (currentNode.right != null) {
                        deque.addFirst(currentNode.right);
                    }

                } else {
                    currentNode = deque.pollFirst();

                    if (currentNode.right != null) {
                        deque.addLast(currentNode.right);
                    }
                    if (currentNode.left != null) {
                        deque.addLast(currentNode.left);
                    }
                }

                levelRes.add(currentNode.val);
            }

            res.add(levelRes);
            currentLevel++;

        }

        return res;
    }
}
// @lc code=end

