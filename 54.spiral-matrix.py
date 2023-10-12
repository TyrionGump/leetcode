#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        row_begin = 0
        row_end = len(matrix)- 1
        col_begin = 0
        col_end = len(matrix[0]) - 1

        while row_begin <= row_end and col_begin <= col_end:
            for col in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][col])
            row_begin += 1

            for row in range(row_begin, row_end + 1):
                res.append(matrix[row][col_end])
            col_end -= 1

            if row_begin <= row_end:
                for col in range(col_end, col_begin - 1, -1):
                    res.append(matrix[row_end][col])
                row_end -= 1
            
            if col_begin <= col_end:  
                for row in range(row_end, row_begin - 1, -1):
                    res.append(matrix[row][col_begin])
                col_begin += 1
        
        return res
                

        
            

# @lc code=end

