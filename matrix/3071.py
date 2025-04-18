class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        '''
        rest of the grid: count values in every cell 

        Y - decrement value in rest of the grid ^ 
        count left to right diagonal 
        count right to left diagonal 
        count middle stem 

        for each alternating value in Y and rest of the grid: 
        - calculate change needed and store min number of changes 

        Time: O(n * n)
        Space: O(3) -> creating array size 3 for grid values 
        '''
        entireGrid = [0] * 3 
        y = [0] * 3 
        ans = inf
        n = len(grid) 
        center = len(grid) // 2 

        # count values in grid 
        for r in range(n):
            for c in range(n):
                entireGrid[grid[r][c]] += 1 
        
        # count Y diagonal 
        for i in range(center):
            left = i 
            right = n - i - 1 
            y[grid[i][left]] += 1 
            y[grid[i][right]] += 1 
            # decrement entireGrid 
            entireGrid[grid[i][left]] -= 1 
            entireGrid[grid[i][right]] -= 1 
        
        # count Y stem 
        for i in range(center, n):
            y[grid[i][center]] += 1 
            entireGrid[grid[i][center]] -= 1 
        
        # calculate changes on alternating values 
        for i in range(3):
            for j in range(3):
                if i != j:
                    yChanges = sum(y) - y[i] 
                    gridChanges = sum(entireGrid) - entireGrid[j] 
                    ans = min(ans, yChanges + gridChanges) 
        
        return ans 