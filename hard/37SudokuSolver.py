class Solution:
    sudokuSolved = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def checkBoard():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return False
            return True
        def placeNextNumber():
            if checkBoard():
                self.sudokuSolved = True
            else:
                bestRow, bestColumn, bestPossibleNumbers, result = getBestPosition()
                if result:
                    backtrack(bestRow, bestColumn, bestPossibleNumbers)
          

        def couldPlace(d, row, col):
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])

        def placeNumber(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def removeNumber(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
        
        def backtrack(row, col, numbers):
            for d in numbers:
                if couldPlace(d, row, col):
                    placeNumber(d, row, col)
                    placeNextNumber()
                    if not self.sudokuSolved:
                        removeNumber(d, row, col)
        
        def getPossibleNumbers(row, column) -> List[int]:
            output = []   
            for i in range(1,10):
                if couldPlace(i, row, column):
                   output.append(i)
            return output
            
            
        def getBestPosition():
            minNumber = 10
            bestRow =None
            bestColumn = None
            bestPossibleNumbers = None
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        possibleNumbers = getPossibleNumbers(i, j)
                        if len(possibleNumbers) == 0:
                            return 0, 0, [], False
                        if len(possibleNumbers)<minNumber:
                            minNumber = len(possibleNumbers)
                            bestRow = i 
                            bestColumn = j
                            bestPossibleNumbers = possibleNumbers


            return bestRow, bestColumn, bestPossibleNumbers, True
         
        N = 9
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        box_index = lambda row, col: (row // 3 ) * 3 + col // 3
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    placeNumber(d, i, j)
        bestRow, bestColumn, bestPossibleNumbers, result = getBestPosition()
        backtrack(bestRow, bestColumn, bestPossibleNumbers)
