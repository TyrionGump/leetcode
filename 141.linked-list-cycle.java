/*
 * @lc app=leetcode id=141 lang=java
 *
 * [141] Linked List Cycle
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            head = head.next;
            fast = fast.next.next;

            if (fast == head) {
                return true;
            }

        }

        return false;
    }
}
// @lc code=end

