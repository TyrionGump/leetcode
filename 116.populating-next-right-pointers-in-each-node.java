/*
 * @lc app=leetcode id=116 lang=java
 *
 * [116] Populating Next Right Pointers in Each Node
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        
        if (root == null) {
            return null;
        }

        Node levelStart = root;
        Node currentNode;

        while (levelStart.left != null) {
            currentNode = levelStart;

            while (currentNode != null) {
                currentNode.left.next = currentNode.right;

                if (currentNode.next != null) {
                    currentNode.right.next = currentNode.next.left;
                }

                currentNode = currentNode.next;
            }

            levelStart = levelStart.left;
        }

        return root;
    }
}
// @lc code=end

