class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        rotate groups of 4 cells by layer

        Time: O(n*n // 4) 
        Space: O(1)  
        """
        left, right = 0, len(matrix[0]) - 1 

        while left <= right:
            for i in range(right - left):
                top, bottom = left, right 
                top_left = matrix[top][left + i] 

                # move bottom left to top left 
                matrix[top][left + i] = matrix[bottom - i][left]
                # move bottom right to bottom left 
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move top right to bottom right  
                matrix[bottom][right - i] = matrix[top + i][right] 
                # move prev top left to top right 
                matrix[top + i][right] = top_left 

            left += 1 
            right -= 1 