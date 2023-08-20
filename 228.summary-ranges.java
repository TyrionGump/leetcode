/*
 * @lc app=leetcode id=228 lang=java
 *
 * [228] Summary Ranges
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        
        int numsLength = nums.length;

        if (numsLength == 0) {
            return List.of();
        }

        List<String> res = new ArrayList<>();
        int rangeStartIndex = 0;

        for (int i = 0; i < numsLength - 1; i++) {
            if (nums[i + 1] - nums[i] != 1) {
                if (rangeStartIndex == i) {
                    res.add(String.valueOf(nums[i]));
                } else {
                    res.add(String.format("%d->%d", nums[rangeStartIndex], nums[i]));
                }

                rangeStartIndex = i + 1;
            }
        }

        if (rangeStartIndex == numsLength - 1) {
            res.add(String.valueOf(nums[rangeStartIndex]));
        } else {
            res.add(String.format("%d->%d", nums[rangeStartIndex], nums[numsLength - 1]));
        }

        return res;
    }
}
// @lc code=end

