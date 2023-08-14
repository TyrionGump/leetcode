/*
 * @lc app=leetcode id=203 lang=java
 *
 * [203] Remove Linked List Elements
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return null;
        }
        
        // Recursion consumes too much mem
        // head.next = this.removeElements(head.next, val);
        // return head.val == val ? head.next : head;

        ListNode dummyHead = new ListNode();
        ListNode prev = dummyHead;
        ListNode cur = head;

        while (cur != null) {
            if (cur.val != val) {
                prev.next = cur;
                prev = cur;
            } else {
                prev.next = null;  // Prevent the last element val equals to val
            }
            cur = cur.next;
        }

        return dummyHead.next;
    }
}
// @lc code=end

