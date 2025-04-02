class Solution:
    def drop(self, board):
        # vertically shift down by swapping number with lowest 0 
        row, col = len(board), len(board[0])
        
        for c in range(col):
            lowest_zero = -1 
            # iterate from bottom to top 
            for r in range(row - 1, -1, -1):
                if board[r][c] == 0:
                    lowest_zero = max(lowest_zero, r)
                elif lowest_zero >= 0:
                    board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c] 
                    lowest_zero -= 1 

        
    
    def crushCandies(self, board):
        # scan board and change cells to negative
        complete = True 
        candies_to_crush = set() 
        row, col = len(board), len(board[0])

        # scan vertically adj candies 
        for r in range(1, row - 1):
            for c in range(col):
                if board[r][c] == 0:
                    continue 
                if abs(board[r][c]) == abs(board[r-1][c]) == abs(board[r+1][c]):
                    candies_to_crush.update([(r, c), (r-1, c), (r+1, c)])
                    board[r][c] = -abs(board[r][c])
                    board[r-1][c] = -abs(board[r-1][c])
                    board[r+1][c] = -abs(board[r+1][c])
                    complete = False

        # horizontally adj candies 
        for r in range(row):
            for c in range(1, col - 1):
                if board[r][c] == 0:
                    continue 
                if abs(board[r][c]) == abs(board[r][c-1]) == abs(board[r][c+1]):
                    candies_to_crush.update([(r, c), (r, c-1), (r, c+1)])
                    board[r][c] = -abs(board[r][c])
                    board[r][c-1] = -abs(board[r][c-1])
                    board[r][c+1] = -abs(board[r][c+1])
                    complete = False

        # change values to 0
        for r, c in candies_to_crush:
            board[r][c] = 0 

        return complete



    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        '''
        problem: restore board to stable state 
        - crush candies adjacent 
        - drop candy if empty space (no new candies will drop) 
        - repeat steps until all adj candies on board are crushed 

        brute force -> in-place 
        '''
        row, col = len(board), len(board[0])

        while not self.crushCandies(board):
            self.drop(board)

        return board 