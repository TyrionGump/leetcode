#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Traveral from nodes at the boundary
        height = len(board)
        width = len(board[0])

        for col_idx in range(width):
            if board[0][col_idx] == "O":
                self.BFS(board, 0, col_idx)
            if board[height - 1][col_idx] == "O":
                self.BFS(board, height - 1, col_idx)
        
        for row_idx in range(height):
            if board[row_idx][0] == "O":
                self.BFS(board, row_idx, 0)
            if board[row_idx][width - 1] == "O":
                self.BFS(board, row_idx, width - 1)
        
        for row_idx in range(height):
            for col_idx in range(width):
                if board[row_idx][col_idx] == "*":
                    board[row_idx][col_idx] = "O"
                elif board[row_idx][col_idx] == "O":
                    board[row_idx][col_idx] = "X"
    
    def BFS(self, board, row_idx, col_idx):
        height = len(board)
        width = len(board[0])

        q = deque()
        q.append((row_idx, col_idx))
        while q:
            row_idx, col_idx = q.popleft()
            if board[row_idx][col_idx] == "O":
                board[row_idx][col_idx] = "*"

                if 0 <= row_idx - 1 <= height - 1 and 0 <= col_idx <= width - 1:
                    q.append((row_idx - 1, col_idx))
                if 0 <= row_idx <= height - 1 and 0 <= col_idx + 1 <= width - 1:
                    q.append((row_idx, col_idx + 1))
                if 0 <= row_idx + 1 <= height - 1 and 0 <= col_idx <= width - 1:
                    q.append((row_idx + 1, col_idx))
                if 0 <= row_idx <= height - 1 and 0 <= col_idx - 1 <= width - 1:
                    q.append((row_idx, col_idx - 1))    
        
# @lc code=end

