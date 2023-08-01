/*
 * @lc app=leetcode id=160 lang=java
 *
 * [160] Intersection of Two Linked Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
        if (headA == null || headB == null) {
            return null;
        }

        ListNode cursorA = headA;
        ListNode cursorB = headB;

        while (cursorA != cursorB) {
            cursorA = cursorA == null ? headB : cursorA.next;
            cursorB = cursorB == null ? headA : cursorB.next;
        }

        return cursorA;
    }
}
// @lc code=end

