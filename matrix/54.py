class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Time: O(N * M)
        Space: O(1) 
        '''
        ans = [] 
        top, bottom = 0, len(matrix) - 1 
        left, right = 0, len(matrix[0]) - 1 

        while top <= bottom and left <= right:
            # iterate top row 
            for i in range(left, right + 1):
                ans.append(matrix[top][i]) 
            top += 1 

            # right col 
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right]) 
            right -= 1 

            if top <= bottom:
                # bottom in reverse
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1 
            
            # left col  
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1 
        
        return ans 