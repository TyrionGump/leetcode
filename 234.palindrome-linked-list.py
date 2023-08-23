#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur_node = slow
        prev_node = slow.next
        cur_node.next = None

        while prev_node:
            temp = prev_node.next
            prev_node.next = cur_node
            cur_node = prev_node
            prev_node = temp


        
        left = head
        right = cur_node

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
# @lc code=end

