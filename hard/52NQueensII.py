class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def isSafe(col, row, board) -> bool:
            for i in range(0, row):
                if board[i][col] == 'Q':
                    return False
            for i in range(0, col):
                if board[row][i] == 'Q':
                    return False
            i = row - 1
            j = col - 1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            i = row+1
            j = col-1
            while i<n and j>=0:
                if board[i][j] == 'Q':
                    return False
                i+=1
                j-=1
            return True

        def helper(col, board, counter):
            if col == n:
                counter[0] +=1
                print(board)
                return
            for row in range(n):
                if isSafe(col, row, board):
                    board[row][col] = 'Q'
                    helper(col+1, board, counter)
                    board[row][col] = '.'
         
        board = [["."]*n for _ in range(n)]
        counter = [0] 
        helper(0, board, counter)
        return counter[0]

        






        

           



        
