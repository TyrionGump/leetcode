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

        # Compare the greatest num in each list
        l_tail = m - 1
        r_tail = n - 1

        while l_tail >= 0 and r_tail >= 0:
            if (nums1[l_tail] > nums2[r_tail]):
                nums1[l_tail + r_tail + 1] = nums1[l_tail]
                l_tail -= 1
            else:
                nums1[l_tail + r_tail + 1] = nums2[r_tail]
                r_tail -= 1
        
        if r_tail >= 0:
            nums1[:r_tail + 1] = nums2[:r_tail + 1]



        


# @lc code=end

