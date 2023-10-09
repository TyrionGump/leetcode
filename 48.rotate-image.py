#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()
        cols = len(matrix)

        for i in range(cols):
            for j in range(i + 1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
# @lc code=end

