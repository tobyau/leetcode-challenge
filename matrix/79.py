class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        DFS if cell matches first letter of the word 
        similar to find islands 

        Time: O(n * m * 3^L) -> length of board * 3 directions since we won't go back to previous cells  
        Space: O(word)
        '''
        def withinBounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c, index):
            # match the whole word
            if index == len(word):
                return True 

            if not withinBounds(r, c) or board[r][c] != word[index]:
                return False
            
            # mark visited 
            temp, board[r][c] = board[r][c], '#'

            # explore neighbors 
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    return True 
            
            # restore original value 
            board[r][c] = temp 
            return False
        
        rows, cols = len(board), len(board[0]) 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True 

        return False 