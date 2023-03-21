#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # First Idea: Merge Sort
        # res = []
        # nums1[m:] = nums2
        
        # i = 0
        # j = m
        # while i <= m-1 and j <= m+n-1:
        #     if nums1[i] > nums1[j]:
        #         res.append(nums1[j])
        #         j += 1
        #     else:
        #         res.append(nums1[i])
        #         i += 1
        
        # if i <= m-1:
        #     res.extend(nums1[i:m])
        
        # if j <= m+n-1:
        #     res.extend(nums1[j:])
        
        # nums1[:] = res
        # Solution in discussion
        # nums1[m:] = nums2
        # nums1.sort()


        


# @lc code=end

