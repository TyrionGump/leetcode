#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # for row in matrix:
        #     if target >= row[0] and target <= row[-1]:
        #         return target in row
        
        # return False

        height = len(matrix)
        width = len(matrix[0])
        l = 0
        r = height * width - 1
        while l <= r:
            mid = (l + r) // 2
            mid_row = mid // width
            mid_col = mid % width
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
# @lc code=end

