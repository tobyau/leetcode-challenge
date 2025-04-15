class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        count rotten oranges, run BFS on rotten oranges 
        each level is 1 min 
        '''
        rows, cols = len(grid), len(grid[0]) 
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        fresh = 0 
        mins = 0 

        # count fresh oranges 
        # store rotten oranges in q 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))  
                elif grid[r][c] == 1:
                    fresh += 1 
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            mins += 1 

        return mins if fresh == 0 else -1 