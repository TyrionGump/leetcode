/*
 * @lc app=leetcode id=148 lang=java
 *
 * [148] Sort List
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
    public ListNode sortList(ListNode head) {
        
        if (head == null || head.next == null) {
            return head;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode mid = slow.next;
        slow.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(mid);

        return mergeSort(left, right);

    }

    private ListNode mergeSort(ListNode left, ListNode right) {

        ListNode dummyHead = new ListNode();
        ListNode currentNode = dummyHead;

        while (left != null && right != null) {
            
            if (left.val < right.val) {
                currentNode.next = left;
                left = left.next;
            } else {
                currentNode.next = right;
                right = right.next;
            }

            currentNode = currentNode.next;
        }

        if (left != null) {
            currentNode.next = left;
        }

        if (right != null) {
            currentNode.next = right;
        }

        return dummyHead.next;
    }
}
// @lc code=end

