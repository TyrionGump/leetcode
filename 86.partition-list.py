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
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head:
            if head.val < x:
                prev = head
                head = head.next
            else:
                while head.next and head.next.val >= x:
                    head = head.next

                # If a node with value < x is found, move it after 'prev'
                if head.next:  # means head.next.val < x
                    temp = head.next
                    head.next = temp.next
                    temp.next = prev.next
                    prev.next = temp
                    prev = temp
                else:
                    break

        return dummy.next


        
# @lc code=end

