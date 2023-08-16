import collections
class Solution:
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                print(board[i][j])
                if board[i][j] == ".":
                    
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(int(i/3),int(j/3))]:
                    return False 
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(int(i/3),int(j/3))].add(board[i][j])
        return True
z = Solution()

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(z.isValidSudoku(board))
