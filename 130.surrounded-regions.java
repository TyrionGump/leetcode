/*
 * @lc app=leetcode id=130 lang=java
 *
 * [130] Surrounded Regions
 */

// @lc code=start

class Solution {
    private char[][] board;
    private int height;
    private int width;

    public void solve(char[][] board) {
        this.board = board;
        height = board.length;
        width = board[0].length;

        for(int rowIndex = 0; rowIndex < height; rowIndex++) {
            if (this.board[rowIndex][0] == 'O') {
                BFS(rowIndex, 0);
            }

            if (this.board[rowIndex][width - 1] == 'O') {
                BFS(rowIndex, width - 1);
            }
        }

        for (int colIndex = 0; colIndex < width; colIndex++) {
            if (this.board[0][colIndex] == 'O') {
                BFS(0, colIndex);
            }

            if (this.board[height - 1][colIndex] == 'O') {
                BFS(height - 1, colIndex);
            }
        }

        for (int rowIndex = 0; rowIndex < height; rowIndex++) {
            for (int colIndex = 0; colIndex < width; colIndex++) {
                if (this.board[rowIndex][colIndex] == '*') {
                    this.board[rowIndex][colIndex] = 'O';
                } else if (this.board[rowIndex][colIndex] == 'O') {
                    this.board[rowIndex][colIndex] = 'X';
                }
            }
        }

    }

    // private void BFS(int rowIndex, int colIndex) {
    //     Deque<List<Integer>> queue = new ArrayDeque<>();
    //     queue.addLast(List.of(rowIndex, colIndex));

    //     while (!queue.isEmpty()) {
    //         List<Integer> coord = queue.pollLast();
    //         rowIndex = coord.get(0);
    //         colIndex = coord.get(1);
            
    //         if (board[rowIndex][colIndex] == 'O') {
    //             board[rowIndex][colIndex] = '*';
                
    //             if (rowIndex - 1 >= 0 && rowIndex - 1 <= height - 1 && colIndex >= 0 && colIndex <= width - 1) {
    //                 queue.addLast(List.of(rowIndex - 1, colIndex));
    //             }

    //             if (rowIndex >= 0 && rowIndex <= height - 1 && colIndex + 1 >= 0 && colIndex + 1 <= width - 1) {
    //                 queue.addLast(List.of(rowIndex, colIndex + 1));
    //             }

    //             if (rowIndex + 1 >= 0 && rowIndex + 1 <= height - 1 && colIndex >= 0 && colIndex <= width - 1) {
    //                 queue.addLast(List.of(rowIndex + 1, colIndex));
    //             }

    //             if (rowIndex >= 0 && rowIndex <= height - 1 && colIndex - 1 >= 0 && colIndex - 1 <= width - 1) {
    //                 queue.addLast(List.of(rowIndex, colIndex - 1));
    //             }
    //         }
    //     }
        
    // }

    private void BFS(int rowIndex, int colIndex) {
        if (rowIndex < 0 || rowIndex > height - 1 || colIndex < 0 || colIndex > width - 1) {
            return;
        }

        if (board[rowIndex][colIndex] == 'O') {
            board[rowIndex][colIndex] = '*';
            BFS(rowIndex - 1, colIndex);
            BFS(rowIndex, colIndex + 1);
            BFS(rowIndex + 1, colIndex);
            BFS(rowIndex, colIndex - 1);
        }
        
    }
}
// @lc code=end

