#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Version 1.0
        res = ListNode()
        pointer = res
        while l1 or l2 :
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            digit = (pointer.val + l1_val + l2_val) % 10
            ten = (pointer.val + l1_val + l2_val) // 10

            pointer.val = digit

            if ten > 0:
                pointer.next = ListNode(val=ten)
            elif l1 is None and l2 is None:
                break
            else:
                pointer.next = ListNode()
            pointer = pointer.next
        return res

        # carry = 0
        # res = ListNode()
        # pointer = res
        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next
        #     pointer.val = carry % 10
        #     if l1 is None and l2 is None and carry//10 == 0:
        #         break
        #     else:
        #         pointer.next = ListNode(carry//10)
        #         pointer = pointer.next
        #         carry //=10
        # return res



            

        
# @lc code=end

