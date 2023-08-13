/*
 * @lc app=leetcode id=202 lang=java
 *
 * [202] Happy Number
 */

// @lc code=start
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = sumDigits(n);

        while (fast != slow) {
            slow = sumDigits(slow);
            fast = sumDigits(sumDigits(fast));
        }

        return fast == 1;
    }

    public int sumDigits(int n) {
        int sum = 0;

        while (n > 0) {
            int reminder = n % 10;
            sum += reminder * reminder;
            n /= 10; 
        }

        return sum;
    }
}
// @lc code=end

