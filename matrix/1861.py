class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        '''
        create empty grid and populate it ( n x m ) 

        shift stones to the right while keeping track of curr pointer 
        '''
        rows, cols = len(boxGrid), len(boxGrid[0]) 
        res = [["."] * rows for _ in range(cols)]

        for r in range(rows):
            # keep track of curr position when changing stones or obstacles 
            i = cols - 1
            for c in range(cols - 1, -1, -1):
                if boxGrid[r][c] == "#":
                    res[i][rows - r - 1] = "#"
                    i -= 1 
                elif boxGrid[r][c] == "*":
                    res[c][rows - r - 1] = "*"
                    i = c - 1 
        
        return res 