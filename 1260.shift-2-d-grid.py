#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # # First idea: flatten the matrix and rebuild
        # h = len(grid)
        # w = len(grid[0])

        # shifted = []
        # for ls in grid:
        #     shifted.extend(ls)
        
        # k %= len(shifted)

        # cut_idx = len(shifted) - k
        # left = shifted[:cut_idx]
        # right = shifted[cut_idx:]
        # shifted[:] = right + left

        # for i in range(h):
        #     grid[i] = shifted[i*w:(i+1)*w]
        # return grid

        # Second idea: create a matrix and cal pos based on // and %
        h = len(grid)
        w = len(grid[0])
        res = []
        for i in range(h):
            res.append([])
            for j in range(w):
                res[i].append([])

        k %= h * w
        print(h, w)
        for i in range(h):
            for j in range(w):
                idx = (i*w+j+k) % (h * w)
                new_row = idx // w
                new_col = idx % w
                res[new_row][new_col] = grid[i][j]
        
        return res
                
        
# @lc code=end

