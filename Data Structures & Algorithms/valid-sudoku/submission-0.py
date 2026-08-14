class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check every row
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        # 2. Check every column
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        # 3. Check every 3x3 sub-box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        cell = board[r][c]
                        if cell == ".":
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)

        return True

        