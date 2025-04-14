class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols - 1 
        top, bottom = 0, rows - 1 
        res = [] 

        while top <= bottom and left <= right:
            # iterate top 
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 
            # iterate right 
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1 
            # iterate bottom in reverse 
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1 
            # iterate left to right 
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1 
        
        return res 