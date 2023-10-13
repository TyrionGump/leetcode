/*
 * @lc app=leetcode id=62 lang=java
 *
 * [62] Unique Paths
 */

// @lc code=start
class Solution {
    public int uniquePaths(int m, int n) {

     int[][] matrix_paths = new int[m][n];

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                
                if (row == 0 || col == 0) {
                    matrix_paths[row][col] = 1;
                } else {
                    matrix_paths[row][col] = matrix_paths[row - 1][col] + matrix_paths[row][col - 1];
                }
                
            }
        }

        return matrix_paths[m - 1][n - 1];
    }
}
// @lc code=end

