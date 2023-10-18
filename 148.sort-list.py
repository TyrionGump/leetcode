#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge_sort(left, right)



    def merge_sort(self, head_1, head_2):

        dummy_head = ListNode()
        curr_node = dummy_head

        while head_1 and head_2:
            if head_1.val < head_2.val:
                curr_node.next = head_1
                head_1 = head_1.next
            else:
                curr_node.next = head_2
                head_2 = head_2.next
            curr_node = curr_node.next
        
        if head_1:
            curr_node.next = head_1
        
        if head_2:
            curr_node.next = head_2
        
        return dummy_head.next
        


        
# @lc code=end

