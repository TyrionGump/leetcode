#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def get_neighbours(self, node, board):
        neighbours = []

        # clockwise: right, down, left, up
        if (node[0], node[1] + 1) != node[2] and node[1] + 1 < len(board[0]):
            neighbours.append((node[0], node[1] + 1, (node[0], node[1])))
        if (node[0] + 1, node[1]) != node[2] and node[0] + 1 < len(board):
            neighbours.append((node[0] + 1, node[1], (node[0], node[1])))
        if (node[0], node[1] - 1) != node[2] and node[1] - 1 >= 0:
            neighbours.append((node[0], node[1] - 1, (node[0], node[1])))
        if (node[0] - 1, node[1]) != node[2] and node[0] - 1 >= 0:
            neighbours.append((node[0] - 1, node[1], (node[0], node[1])))
        
        return neighbours

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                word_idx = 0
                q = [(row_idx, col_idx, None)]
                while q:
                    cur_node = q.pop()
                    print(cur_node)
                    if board[cur_node[0]][cur_node[1]] == word[word_idx]:
                        word_idx += 1
                        for n in self.get_neighbours(cur_node, board):
                            q.append(n)
                    
                    if word_idx == len(word):
                        return True
        
        return False
        
# @lc code=end

