/*
 * @lc app=leetcode id=66 lang=java
 *
 * [66] Plus One
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        
        int digitsSize = digits.length;

        for (int i = digitsSize - 1; i >= 0; i--) {
            if (digits[i] + 1 < 10) {
                digits[i] += 1;
                return digits;
            } else {
                digits[i] = 0;
            }
        }

        int[] extenedRes = new int[digitsSize + 1];
        extenedRes[0] = 1;
        return extenedRes;
    }
}
// @lc code=end

