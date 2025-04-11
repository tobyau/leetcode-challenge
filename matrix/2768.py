class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        '''
        - in an m*n grid => (m-1) * (n-1) possible 2x2 grids 
        - each black cell may affect 4 different 2x2 blocks 

        problem: how many 2x2 grids contain i black cells? 

        Time: O(b) -> number of black cells 
        Space: O(u) -> number of unique 2x2 blocks affected by black cells 
        '''
        counts = defaultdict(int) 

        for x, y in coordinates:
            # handle 2x2 top left corners 
            for dx in [0, -1]:
                for dy in [0, -1]:
                    i, j = x + dx, y + dy 
                    if 0 <= i < m - 1 and 0 <= j < n - 1:
                        counts[(i, j)] += 1 
        
        ans = [0] * 5 
        for count in counts.values():
            ans[count] += 1 
        
        total_blocks = (m - 1) * (n - 1)
        ans[0] = total_blocks - sum(ans[1:])

        return ans 