/*
 * @lc app=leetcode id=205 lang=java
 *
 * [205] Isomorphic Strings
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Character> s2t = new HashMap<>();
        Map<Character, Character> t2s = new HashMap<>();

        for(int i = 0; i < s.length(); i++) {

            char charOfs = s.charAt(i);
            char charOft = t.charAt(i);


            if (s2t.containsKey(charOfs)) {
                if (s2t.get(charOfs) != charOft) {
                    return false;
                }
            } else {
                s2t.put(charOfs, charOft);
            }

            if (t2s.containsKey(charOft)) {
                if (t2s.get(charOft) != charOfs) {
                    return false;
                }
            } else {
                t2s.put(charOft, charOfs);
            }
        }

        return true;
    }
}
// @lc code=end

