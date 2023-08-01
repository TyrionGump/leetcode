#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        cursorA = headA
        cursorB = headB

        while cursorA != cursorB:
            cursorA = cursorA.next if cursorA else headB
            cursorB = cursorB.next if cursorB else headA
        
        return cursorA
        
# @lc code=end

