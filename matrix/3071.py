class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        countY, restGrid = [0] * 3, [0] * 3 
        n = len(grid) 
        center = n // 2 
        res = inf 

        # count grid 
        for r in range(n):
            for c in range(n):
                restGrid[grid[r][c]] += 1 

        # count Y diagonals - left right 
        for i in range(center):
            left_diag = i 
            right_diag = n - i - 1 
            countY[grid[i][left_diag]] += 1 
            restGrid[grid[i][left_diag]] -= 1 
            countY[grid[i][right_diag]] += 1 
            restGrid[grid[i][right_diag]] -= 1 
        
        # count Y stem 
        for i in range(center, n):
            countY[grid[i][center]] += 1 
            restGrid[grid[i][center]] -= 1 
        
        # compare 
        for i in range(3):
            for j in range(3):
                if i != j:
                    changeY = sum(countY) - countY[i]
                    changeRest = sum(restGrid) - restGrid[j] 
                    res = min(res, changeY + changeRest)
        
        return res 