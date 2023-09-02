/*
 * @lc app=leetcode id=105 lang=java
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 */

// @lc code=start

import java.util.Map;

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
    private int[] preorder;
    private int[] inorder;
    private Map<Integer, Integer> nodeToIdxInOrder;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        nodeToIdxInOrder = new HashMap<>(inorder.length);

        for(int i = 0; i < inorder.length; i++) {
            nodeToIdxInOrder.put(inorder[i], i);
        }

        return build(0, 0, inorder.length - 1);
    }

    private TreeNode build(int preStart, int inStart, int inEnd) {
        if (inStart > inEnd) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = nodeToIdxInOrder.get(root.val); 

        int leftTreeSize = inIndex - inStart;

        root.left = build(preStart + 1, inStart, inIndex - 1);
        root.right = build(preStart + leftTreeSize + 1, inIndex + 1, inEnd);

        return root;
    }
}

// @lc code=end

