/*
 * @lc app=leetcode id=566 lang=java
 *
 * [566] Reshape the Matrix
 */

// @lc code=start
class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int originalRowSize = mat.length;
        int originalColSize = mat[0].length;

        if (originalColSize * originalRowSize != r * c) {
            return mat;
        }

        int[][] res = new int[r][c];
        int rowTracker = 0;
        int colTracker = 0;

        for (int rowIdx = 0; rowIdx < originalRowSize; rowIdx++) {
            for (int colIdx = 0; colIdx < originalColSize; colIdx++) {
                if (colTracker == c) {
                    rowTracker++;
                    colTracker = 0;
                }

                res[rowTracker][colTracker] = mat[rowIdx][colIdx];
                colTracker++;
                
            }
        }

        return res;
    }
}
// @lc code=end

