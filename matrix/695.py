class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        DFS on regions with 1 
        '''
        rows, cols = len(grid), len(grid[0]) 
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        max_area = 0 

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            
            area = 1 
            grid[r][c] = -1 
            
            for dr, dc in directions:
                area += dfs(r + dr, c + dc) 
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_area = dfs(r, c) 
                    max_area = max(max_area, curr_area) 

        return max_area
            
