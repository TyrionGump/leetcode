/*
 * @lc app=leetcode id=414 lang=java
 *
 * [414] Third Maximum Number
 */

// @lc code=start
class Solution {
    public int thirdMax(int[] nums) {
        Integer firstMax = null;
        Integer secondMax = null;
        Integer thirdMax = null;

        for (Integer val : nums) {
            if (val.equals(firstMax) || val.equals(secondMax) || val.equals(thirdMax)) {
                continue;
            }


            if (firstMax == null || val > firstMax) {
                thirdMax = secondMax;
                secondMax = firstMax;
                firstMax = val;
            } else if (secondMax == null || val > secondMax) {
                thirdMax = secondMax;
                secondMax = val;
            } else if (thirdMax == null || val > thirdMax) {
                thirdMax = val;
            }
        }



        if (thirdMax != null) {
            return thirdMax;
        } else {
            return firstMax;
        }
    }
}
// @lc code=end

