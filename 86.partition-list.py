#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lower_dummy = ListNode()
        upper_dummy = ListNode()

        lower_pointer = lower_dummy
        upper_pointer = upper_dummy

        while head:
            if head.val < x:
                lower_pointer.next = head
                lower_pointer = lower_pointer.next
            else:
                upper_pointer.next = head
                upper_pointer = upper_pointer.next
            head = head.next
        
        upper_pointer.next = None
        lower_pointer.next = upper_dummy.next

        return lower_dummy.next
            


        
# @lc code=end

