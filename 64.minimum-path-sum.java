/*
 * @lc app=leetcode id=64 lang=java
 *
 * [64] Minimum Path Sum
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public int minPathSum(int[][] grid) {
        int rowSize = grid.length;
        int colSize = grid[0].length;

        int[][] pathMatrix = new int[rowSize][colSize];

        pathMatrix[0][0] = grid[0][0];

        for (int row = 1; row < rowSize; row++) {
            pathMatrix[row][0] = pathMatrix[row - 1][0] + grid[row][0];
        }

        for (int col = 1; col < colSize; col++) {
            pathMatrix[0][col] = pathMatrix[0][col - 1] + grid[0][col];
        }
        
        for (int row = 1; row < rowSize; row++) {
            for (int col = 1; col < colSize; col++) {
                pathMatrix[row][col] = Math.min(pathMatrix[row - 1][col], pathMatrix[row][col - 1]) + grid[row][col];
            }
        }

        return pathMatrix[rowSize - 1][colSize - 1];

    }
}
// @lc code=end

