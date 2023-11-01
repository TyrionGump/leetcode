#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        idx = 0
        available = 0
        flowerbed_size = len(flowerbed)

        while (idx < flowerbed_size):
            prev = 0 if idx == 0 else flowerbed[idx - 1]
            next = 0 if idx == flowerbed_size - 1 else flowerbed[idx + 1]
            if flowerbed[idx] == 0 and prev == 0 and next == 0:
                available += 1
                idx += 2
            else:
                idx += 1
            
            if available >= n:
                return True
        
        return False

                
# @lc code=end

