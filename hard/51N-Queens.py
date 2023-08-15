class Solution:
    
    def isSafe(self, row, col, n , board):
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        i, j = row, col
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i-=1
            j-=1
        i, j = row, col
        while i<n and j>=0:
            if board[i][j] == 'Q':
                return False
            i+=1
            j-=1
        return True

    def helper(self, col, n, board, output):
        if col == n:
            output.append(["".join(i) for i in board])
            return
        for row in range(n):
            if self.isSafe(row, col, n , board):
                board[row][col] = "Q"
                self.helper(col+1, n, board, output)
                board[row][col] = "."
        return

    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for i in range(n)]
        output = []
        self.helper(0, n, board, output)
        return output
