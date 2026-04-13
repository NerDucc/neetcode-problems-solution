class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            grid_idx = 3
            for j in range(9):
                if board[i][j] in row and board[i][j] != '.':
                    return False
                elif board[j][i] in col and board[j][i] != '.':
                    return False
                else:
                    row.add(board[i][j])
                    col.add(board[j][i])
        for grid_idx_row in range(0, 9, 3):
            for grid_idx_col in range(0 ,9, 3):
                grid = set()
                for i in range(3):
                    for j in range(3):
                        val = board[grid_idx_row + i][grid_idx_col + j]
                        if val != '.':
                            if val in grid:
                                return False
                            grid.add(val)
        return True
        