/*
 * @lc app=leetcode id=1002 lang=java
 *
 * [1002] Find Common Characters
 */

// @lc code=start

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

class Solution {
    public List<String> commonChars(String[] words) {
        int[] globalCounter = new int[26];
        Arrays.fill(globalCounter, Integer.MAX_VALUE);

        for (String word : words) {
            int [] wordCounter = new int[26];
            word.chars().forEach(c -> wordCounter[c - 'a']++);
            IntStream.range(0, 26).forEach(i -> globalCounter[i] = Math.min(globalCounter[i], wordCounter[i]));
        }

        List<String> res = new ArrayList<>();
        IntStream.range('a', 'z' + 1).forEach(c -> res.addAll(Collections.nCopies(globalCounter[c - 'a'], String.valueOf((char)c))));
        return res;
    }
}
// @lc code=end

