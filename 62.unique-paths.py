#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths_matrix = [[1] * n] * m

        for row in range(1, m):
            for col in range(1, n):
                paths_matrix[row][col] = paths_matrix[row - 1][col] + paths_matrix[row][col - 1]
        
        return paths_matrix[m - 1][n - 1]
# @lc code=end

