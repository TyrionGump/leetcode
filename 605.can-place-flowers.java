/*
 * @lc app=leetcode id=605 lang=java
 *
 * [605] Can Place Flowers
 */

// @lc code=start
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        int currentIdx = 0;
        int availables = 0;
        
        int prev = 0;
        int next = 0;

        while (currentIdx < flowerbed.length) {
            prev = currentIdx == 0 ? 0 : flowerbed[currentIdx - 1];
            next = currentIdx == flowerbed.length - 1 ? 0 : flowerbed[currentIdx + 1];

            if (flowerbed[currentIdx] == 0 && prev == 0 && next == 0) {
                availables++;
                currentIdx += 2;

            } else {
                currentIdx += 1;
            }

            if (availables >= n) {
                    return true;
            }
        }

        return false;
    }
}
// @lc code=end

