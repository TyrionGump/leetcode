#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])

        path_matrix = [[0] * col_size for _ in range(row_size)]

        path_matrix[0][0] = grid[0][0]

        for row in range(1, row_size):
            path_matrix[row][0] = path_matrix[row - 1][0] + grid[row][0]
        for col in range(1, col_size):
            path_matrix[0][col] = path_matrix[0][col - 1] + grid[0][col]
        
        for row in range(1, row_size):
            for col in range(1, col_size):
                path_matrix[row][col] = min(path_matrix[row - 1][col], path_matrix[row][col - 1]) + grid[row][col]
        
        return path_matrix[row_size - 1][col_size - 1]
# @lc code=end

