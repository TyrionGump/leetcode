/*
 * @lc app=leetcode id=70 lang=java
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return n;
        }

        int stepOne = 1;
        int stepTwo = 2;
        int currentStep = 0;

        for(int i = 3; i <= n; i++) {
            currentStep = stepOne + stepTwo;
            stepOne = stepTwo;
            stepTwo = currentStep;
        }

        return stepTwo;

        // int[] steps = new int[n];
        // steps[0] = 1;
        // steps[1] = 2;

        // for(int i = 2; i < n; i++) {
        //     steps[i] = steps[i - 1] + steps[i - 2];
        // }

        // return steps[n - 1];


    }
}
// @lc code=end

