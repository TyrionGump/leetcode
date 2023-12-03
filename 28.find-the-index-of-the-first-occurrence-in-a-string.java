/*
 * @lc app=leetcode id=28 lang=java
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        int haystackLength = haystack.length();
        int needleLength = needle.length();

        if (needleLength > haystackLength) {
            return -1;
        }

        for (int i = 0; i < haystackLength; i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                int haystackPointer = i + 1;
                int needlePointer = 1;

                while (haystackPointer < haystackLength && needlePointer < needleLength) {

                    if (haystack.charAt(haystackPointer) == needle.charAt(needlePointer)) {
                        haystackPointer++;
                        needlePointer++;
                    } else {
                        break;
                    }
                }

                if (needlePointer == needleLength) {
                    return i;
                }
            }
        }

        return -1;
    }
}
// @lc code=end

