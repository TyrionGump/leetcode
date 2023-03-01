/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        // regex may work too much in this problem
        // String[] splitResult = s.split("\\s+");
        // return splitResult[splitResult.length - 1].length();
        
        int lastWordEndIndex = s.length() - 1;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                if (lastWordEndIndex - i != 0) {
                    return lastWordEndIndex - i;
                } else {
                    lastWordEndIndex -= 1;
                }
            }
        }

        if (s.charAt(0) != ' ') {
            return lastWordEndIndex + 1;
        }

        return 0;
    }
}
// @lc code=end

