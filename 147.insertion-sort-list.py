#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode()
        prev = dummy

        while head:
            temp = head.next

            if (prev.val > head.val):
                prev = dummy
            
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            
            head.next = prev.next
            prev.next = head
            head = temp
        
        return dummy.next
# @lc code=end

