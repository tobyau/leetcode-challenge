class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Solution
        - keep track of top, right, bottom, left indicies 

        Time: O(m * n) 
        Space: O(m * n) -> storing all elements in the matrix  
        '''
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1 
        left, right = 0, cols - 1 
        ans = []

        while top <= bottom and left <= right:
            # iterate top 
            for i in range(left, right + 1):
                ans.append(matrix[top][i]) 
            top += 1 
            # iterate right 
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right]) 
            right -= 1 
            # iterate bottom 
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1 
            # iterate left 
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1 
        
        return ans 