#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        is_first_row_zeros = False
        is_first_col_zeros = False
        row_size = len(matrix)
        col_size = len(matrix[0])

        for row in range(row_size):
            if matrix[row][0] == 0:
                is_first_col_zeros = True
                break
        
        for col in range(col_size):
            if matrix[0][col] == 0:
                is_first_row_zeros = True
        
        for row in range(1, row_size):
            for col in range(1, col_size):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, row_size):
            for col in range(1, col_size):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if is_first_col_zeros:
            for row in range(row_size):
                matrix[row][0] = 0
        
        if is_first_row_zeros:
            for col in range(col_size):
                matrix[0][col] = 0
                
            
# @lc code=end

