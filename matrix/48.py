class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        - modify matrix in-place instead.
        - rotate groups of 4 cells (corner) by layer. How? 

        1 2 3       7 4 1 
        4 5 6   =>  8 5 2 
        7 8 9       9 6 3

        Time: O(n*n // 4) 
        Space: O(1)  
        """
        left, right = 0, len(matrix[0]) - 1 

        while left <= right:
            # iterate cols in the layer 
            for i in range(right - left):
                # handle one layer at a time by assigning top and bottom to left and right 
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

            # move to the next layer (inward) 
            left += 1 
            right -= 1 