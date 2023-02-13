import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> resMap = new HashMap<>();
        
        for (int i=0; i < num.length() - 1; i++) {
            resMap.computeIfAbsent(target - nums[i], key -> i);
            
        }
    }
}
// @lc code=end

