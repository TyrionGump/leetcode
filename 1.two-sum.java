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
        
        for (int i = nums.length - 1; i >= 0; i--) {
            Integer secondNumIdx = resMap.get(target - nums[i]);
            if (secondNumIdx != null) {
                return new int[]{i, secondNumIdx};
            } else {
                resMap.put(nums[i], i);
            }
        }
        return null;
    }
}
// @lc code=end

