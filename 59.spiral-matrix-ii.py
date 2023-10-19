#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0 for _ in range(n)] for _ in range(n)]
        counter = 1

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        while bottom >= top and right >= left:

            for col in range(left, right + 1):
                res[top][col] = counter
                counter += 1
            top += 1
            
            for row in range(top, bottom + 1):
                res[row][right] = counter
                counter += 1
            right -= 1

            for col in range(right, left - 1, -1):
                res[bottom][col] = counter
                counter += 1
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                res[row][left] = counter
                counter += 1
            left += 1
        
        return res


                
# @lc code=end

