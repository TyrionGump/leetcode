#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = deque()
        dummy = ListNode()
        dummy.next = head
        curr_node = dummy

        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.next
        
        while n + 1 > 0:
            curr_node = stack.pop()
            n -= 1
        
        curr_node.next = curr_node.next.next
        return dummy.next
            
        
            
# @lc code=end

