class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        DFS
        - run dfs if grid[r][c] == 1 
        - update 1 to # to indicate visited 

        Time: O(m x n) 
        Space: O(m x n)
        '''
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        res = 0 

        def dfs(r, c):
            # if out of bounds return 
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return 
            
            # set visited 
            grid[r][c] = "#"
            
            # dfs on all 4 directions 
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1 
                    dfs(r, c) 
        
        return res 
        
