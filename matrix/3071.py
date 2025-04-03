class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        '''
        solution
        - count Y 
        - count outside of Y 
        '''
        countY = [0] * 3 
        countRest = [0] * 3 
        n = len(grid) 

        # count occurences in grid 
        for i in range(n):
            for j in range(n):
                countRest[grid[i][j]] += 1 
        
        # count Y - left diagonal 
        i, j = 0, 0 
        while i < n//2 and j < n // 2:
            countY[grid[i][j]] += 1 
            countRest[grid[i][j]] -= 1 
            i += 1 
            j += 1 
        
        # right diagonal 
        i, j = 0, n - 1
        while i < n//2 and j > n // 2:
            countY[grid[i][j]] += 1 
            countRest[grid[i][j]] -= 1 
            i += 1 
            j -= 1 
        
        # middle stem 
        for i in range(n//2, n):
            countY[grid[i][n//2]] += 1 
            countRest[grid[i][n//2]] -= 1 

        # calculate sum of changes required to change Y and rest from 0 to 2 
        ans = math.inf 
        for i in range(3):
            for j in range(3):
                if i != j:
                    yChange = sum(countY) - countY[i] 
                    restChange = sum(countRest) - countRest[j] 
                    ans = min(ans, yChange + restChange) 
        
        return ans 