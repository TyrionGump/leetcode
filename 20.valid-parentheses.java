import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Deque;
import java.util.Map;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> rightToLeftBrackets = Map.of('}', '{', ']', '[', ')', '(');

        Set<Character> rightBrackets = rightToLeftBrackets.keySet();
        List<Character> leftBrackets = new ArrayList<>(rightToLeftBrackets.values());

        Deque stack = new ArrayDeque<>();

        for (Character c : s.toCharArray()) {

            if (leftBrackets.contains(c)) {
                stack.add(c);
            } else if (stack.isEmpty() || !stack.pollLast().equals(rightToLeftBrackets.get(c))) {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
// @lc code=end
