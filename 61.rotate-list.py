#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        list_length = 1
        tail = head

        while tail.next:
            list_length += 1
            tail = tail.next
        
        tail.next = head

     
        for _ in range(list_length - k % list_length):
            tail = tail.next
        
        head = tail.next
        tail.next = None

        return head


        
# @lc code=end

