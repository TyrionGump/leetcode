#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row_size = len(obstacleGrid)
        col_size = len(obstacleGrid[0])

        paths_matrix = [[0 for _ in range(col_size)] for _ in range(row_size)]

        if obstacleGrid[0][0] == 1:
            return 0

        paths_matrix[0][0] = 1

        for row in range(1, row_size):
            if obstacleGrid[row][0] == 0:
                paths_matrix[row][0] = paths_matrix[row - 1][0]

        for col in range(1, col_size):
            if obstacleGrid[0][col] == 0:
                paths_matrix[0][col] = paths_matrix[0][col - 1]

        for row in range(1, row_size):
            for col in range(1, col_size):
                if obstacleGrid[row][col] == 0:
                    paths_matrix[row][col] = paths_matrix[row - 1][col] + paths_matrix[row][col - 1]

        return paths_matrix[row_size - 1][col_size - 1]


        
# @lc code=end

