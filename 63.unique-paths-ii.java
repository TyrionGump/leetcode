/*
 * @lc app=leetcode id=63 lang=java
 *
 * [63] Unique Paths II
 */

// @lc code=start
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        int rowSize = obstacleGrid.length;
        int colSize = obstacleGrid[0].length;

        int[][] pathsMatrix = new int[rowSize][colSize];
        
        pathsMatrix[0][0] = 1;

        for (int row = 1; row < rowSize; row++) {
            if (obstacleGrid[row][0] != 1) {
                pathsMatrix[row][0] = pathsMatrix[row - 1][0];
            }
        }

        for (int col = 1; col < colSize; col++) {
            if (obstacleGrid[0][col] != 1) {
                pathsMatrix[0][col] = pathsMatrix[0][col - 1];
            }
        }

        for (int row = 1; row < rowSize; row++) {
            for (int col = 1; col < colSize; col++) {
    
                if (obstacleGrid[row][col] != 1) {
                    pathsMatrix[row][col] = pathsMatrix[row - 1][col] + pathsMatrix[row][col - 1];
                }
            }
        }

        return pathsMatrix[rowSize - 1][colSize - 1];

    }
}
// @lc code=end

