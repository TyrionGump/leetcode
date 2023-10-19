/*
 * @lc app=leetcode id=59 lang=java
 *
 * [59] Spiral Matrix II
 */

// @lc code=start
class Solution {
    public int[][] generateMatrix(int n) {
    
        int [][] res = new int[n][n];
        int top = 0;
        int bottom = n - 1;
        int left = 0;
        int right = n - 1;
        int counter = 1;

        while (left <= right && top <= bottom) {

            for (int col = left; col <= right; col++) {
                res[top][col] = counter;
                counter++;
            }
            top++;

            for (int row = top; row <= bottom; row++) {
                res[row][right] = counter;
                counter++;
            }
            right--;

            for (int col = right; col >= left; col--) {
                res[bottom][col] = counter;
                counter++;
            }
            bottom--;

            for (int row = bottom; row >= top; row--) {
                res[row][left] = counter;
                counter++;
            }
            left++;
        }

        return res;
    }
}
// @lc code=end

