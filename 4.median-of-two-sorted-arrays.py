#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure m > n (just mark the longer one -> n represents the longer one)
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, n, nums2, m = nums2, m, nums1, n
        
        l, r, mid = 0, m, (m + n) // 2
        while l <= r:
            i = (l + r) // 2
            j = mid - i
            if i < m and nums2[j-1] > nums1[i]:
                l = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                r = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j ==0:
                    max_of_left= nums1[i-1]
                else:
                    max_of_left = max(nums2[j-1], nums1[i-1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2

# @lc code=end

