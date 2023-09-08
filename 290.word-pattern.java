/*
 * @lc app=leetcode id=290 lang=java
 *
 * [290] Word Pattern
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");

        if (words.length != pattern.length()) {
            return false;
        }
        
        Map<Character, String> letterToWord = new HashMap<>();
        Map<String, Character> wordToLetter = new HashMap<>();

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            char letter = pattern.charAt(i);

            if (letterToWord.containsKey(letter)) {
                if (!letterToWord.get(letter).equals(word)) {
                    return false;
                }
            } else {
                letterToWord.put(letter, word);
            }

            if (wordToLetter.containsKey(word)) {
                if (!wordToLetter.get(word).equals(letter)) {
                    return false;
                }
            } else {
                wordToLetter.put(word, letter);
            }
        }

        return true;
    }
}
// @lc code=end

