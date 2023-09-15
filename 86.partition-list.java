/*
 * @lc app=leetcode id=86 lang=java
 *
 * [86] Partition List
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
    public ListNode partition(ListNode head, int x) {
        if (head == null) {
            return null;
        }

        ListNode lowerDummy = new ListNode();
        ListNode upperDummy = new ListNode();
        ListNode lowerPointer = lowerDummy;
        ListNode upperPointer = upperDummy;

        while (head != null) {
            if (head.val < x) {
                lowerPointer.next = head;
                lowerPointer = lowerPointer.next;
            } else {
                upperPointer.next = head;
                upperPointer = upperPointer.next;
            }
            head = head.next;
        }

        upperPointer.next = null;
        lowerPointer.next = upperDummy.next;
        
        return lowerDummy.next;
    }
}
// @lc code=end

