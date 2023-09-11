#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev_node = dummy
        cur_node = head

        while cur_node and cur_node.next:
            
            prev_node.next = cur_node.next
            cur_node.next = prev_node.next.next
            prev_node.next.next = cur_node

            prev_node = cur_node
            cur_node = cur_node.next
        
        return dummy.next
            
            
        
# @lc code=end

