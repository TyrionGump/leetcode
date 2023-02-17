
/*
 * @lc app=leetcode id=13 lang=java
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
    public int romanToInt(String s) {
        // Map<Character, Integer> romanToIntMap = Map.of('I', 1, 'V', 5, 'X', 10, 'L', 50, 'C', 100, 'D', 500, 'M', 1000);

        // int res = 0;
        // char[] charArray = s.toCharArray();
        // for(int i = 0; i < charArray.length - 1; i++) {
        //     if (romanToIntMap.get(charArray[i]) < romanToIntMap.get(charArray[i + 1])) {
        //         res -= romanToIntMap.get(charArray[i]);
        //     } else {
        //         res += romanToIntMap.get(charArray[i]);
        //     }
        // }

        // return res + romanToIntMap.get(charArray[charArray.length - 1]);

        int answer = 0, number = 0, prev = 0;

        for (int j = s.length() - 1; j >= 0; j--) {
            switch (s.charAt(j)) {
                case 'M' -> number = 1000;
                case 'D' -> number = 500;
                case 'C' -> number = 100;
                case 'L' -> number = 50;
                case 'X' -> number = 10;
                case 'V' -> number = 5;
                case 'I' -> number = 1;
            }
            if (number < prev) {
                answer -= number;
            } else {
                answer += number;
            }
            prev = number;
        }   
        return answer;
    }
}
// @lc code=end

