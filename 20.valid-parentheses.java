import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Map<Char, Char> rightToLeftBrackets = Map.of('}', '{', ']', '[', ')', '(');

        Set<Char> rightBrackets = rightToLeftBrackets.keyS

        Deque stack = new ArrayDeque<>();

        for (Char c : s.toCharArray()) {
            if 
        }
    }
}
// @lc code=end

