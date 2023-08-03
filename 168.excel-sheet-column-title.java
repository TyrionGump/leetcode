/*
 * @lc app=leetcode id=168 lang=java
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
class Solution {
    public String convertToTitle(int columnNumber) {
        
        StringBuilder res = new StringBuilder();
        
        while (columnNumber > 0) {
            columnNumber--;
            res.append((char)(columnNumber % 26 + 'A'));
            columnNumber = columnNumber / 26;
        }

        return res.reverse().toString();
    }
}
// @lc code=end

