/*
 * @lc app=leetcode id=117 lang=java
 *
 * [117] Populating Next Right Pointers in Each Node II
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
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public Node connect(Node root) {
        
        if (root == null) {
            return null;
        }

        Deque<Node> currentLevelNodes = new ArrayDeque<>();
        currentLevelNodes.add(root);

        while (!currentLevelNodes.isEmpty()) {
            
            int currentLevelSize = currentLevelNodes.size();
            Node previsouNode = null;

            for (int i = 0; i < currentLevelSize; i++) {
                Node currentNode = currentLevelNodes.pollFirst();
                
                if (previsouNode != null) {
                    previsouNode.next = currentNode;
                }

                if (currentNode.left != null) {
                    currentLevelNodes.add(currentNode.left);
                }

                if (currentNode.right != null) {
                    currentLevelNodes.add(currentNode.right);
                }

                previsouNode = currentNode;
            }
        }

        return root;
    }
}
// @lc code=end

