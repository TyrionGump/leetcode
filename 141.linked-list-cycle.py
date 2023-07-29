#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next

            if head is fast:
                return True
        return False
        
# @lc code=end

