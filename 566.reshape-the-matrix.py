#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        original_rows = len(mat)
        original_cols = len(mat[0])
        
        # Early exit if reshaping is not possible
        if original_rows * original_cols != r * c:
            return mat
        
        reshaped_mat = []
        flat_list = []
        for row in mat:
            flat_list.extend(row)
        
        for i in range(0, len(flat_list), c):
            reshaped_mat.append(flat_list[i:i+c])
        
        return reshaped_mat


# @lc code=end

