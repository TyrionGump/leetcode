/*
 * @lc app=leetcode id=73 lang=java
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
class Solution {
    public void setZeroes(int[][] matrix) {
        int rowSize = matrix.length;
        int colSize = matrix[0].length;
        boolean isFirstRowZeros = false;
        boolean isFirstColZeros = false;

        for (int col = 0; col < colSize; col++) {
            if (matrix[0][col] == 0) {
                isFirstRowZeros = true;
                break;
            }
        }

        for (int row = 0; row < rowSize; row++) {
            if (matrix[row][0] == 0) {
                isFirstColZeros = true;
                break;
            }
        }

        for (int row = 1; row < rowSize; row++) {
            for (int col = 1; col < colSize; col++) {
                if (matrix[row][col] == 0) {
                    matrix[0][col] = 0;
                    matrix[row][0] = 0;
                }
            }
        }

        for (int row = 1; row < rowSize; row++) {
            for (int col = 1; col < colSize; col++) {
                if (matrix[0][col] == 0 || matrix[row][0] == 0) {
                    matrix[row][col] = 0;
                }
            }
        }

        if (isFirstColZeros) {
            for (int row = 0; row < rowSize; row++) {
                matrix[row][0] = 0;
            }
        }

        if (isFirstRowZeros) {
            for (int col = 0; col < colSize; col++) {
                matrix[0][col] = 0;
            }
        }

    }
}
// @lc code=end

