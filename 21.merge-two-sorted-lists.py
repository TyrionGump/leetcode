#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # res = ListNode()
        # cur = res

        # while list1 and list2:
        #     if (list1.val < list2.val):
        #         cur.next = ListNode(list1.val)
        #         list1 = list1.next
        #     else:
        #         cur.next = ListNode(list2.val)
        #         list2 = list2.next
            
        #     cur = cur.next
            
        
        # while list1:
        #     cur.next = ListNode(list1.val)
        #     list1 = list1.next
        #     cur = cur.next
        
        # while list2:
        #     cur.next = ListNode(list2.val)
        #     list2 = list2.next
        #     cur = cur.next
        
        # return res.next

        if list1 and list2:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
        
        if not list1:
            return list2
        return list1
        
# @lc code=end

