import collections
def isValidSudoku(board: list[list[str]]) -> bool:
    rowHaz = collections.defaultdict(set)
    colHaz = collections.defaultdict(set)
    sqrz = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            if (
                val in rowHaz[r] or
                val in colHaz[c] or
                val in sqrz[r//3, c//3]
            ):
                return False
            rowHaz[r].add(val)
            colHaz[c].add(val)
            sqrz[r//3, c//3].add(val)

    return True

#---FALSE
board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

#---TRUE
board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board1))
print(isValidSudoku(board2))
