/*
 * @lc app=leetcode id=54 lang=java
 *
 * [54] Spiral Matrix
 */

// @lc code=start

import java.util.ArrayList;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>(matrix.length * matrix[0].length);

        int rowBegin = 0;
        int rowEnd = matrix.length - 1;
        int colBegin = 0;
        int colEnd = matrix[0].length - 1;

        while (rowBegin <= rowEnd && colBegin <= colEnd) {

            for (int col = colBegin; col <= colEnd; col++) {
                res.add(matrix[rowBegin][col]);
            }
            rowBegin++;

            for (int row = rowBegin; row <= rowEnd; row++) {
                res.add(matrix[row][colEnd]);
            }
            colEnd--;

            if (rowBegin <= rowEnd) {
                for (int col = colEnd; col >= colBegin; col--) {
                    res.add(matrix[rowEnd][col]);
                }
            }
            rowEnd--;

            if (colBegin <= colEnd) {
                for (int row = rowEnd; row >= rowBegin; row--) {
                    res.add(matrix[row][colBegin]);
                }
            }
            colBegin++;

        }

        return res;

    }
}
// @lc code=end
