/*
 * @lc app=leetcode id=448 lang=java
 *
 * [448] Find All Numbers Disappeared in an Array
 */

// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Stream;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != nums[nums[i] - 1]) {
                int temp = nums[i];
                nums[i] = nums[temp - 1];
                nums[temp - 1] = temp;
            }
        }

        List<Integer> res = new ArrayList<>();

        for (int i = 1; i <= nums.length; i++) {
            if (i != nums[i - 1]) {
                res.add(i);
            }
        }

        return res;
    }
}
// @lc code=end

