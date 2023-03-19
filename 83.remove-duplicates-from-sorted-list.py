#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion
        # if not head or not head.next:
        #     return head
        
        # head.next = self.deleteDuplicates(head.next)

        # if head.val == head.next.val:
        #     return head.next
        # else:
        #     return head

        # Iteration
        cur_node = head
        while cur_node and cur_node.next:
            if cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
                continue
            cur_node = cur_node.next
        return head
        

# @lc code=end

